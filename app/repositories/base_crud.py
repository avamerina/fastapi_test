from typing import Generic, TypeVar

from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy.orm import Session


T = TypeVar('T')
CreateSchemaType = TypeVar('CreateSchemaType')
UpdateSchemaType = TypeVar('UpdateSchemaType')


class BaseCRUD(Generic[T, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, db: Session, db_model):
        self.db = db
        self.db_model = db_model

    def _execute_with_commit(self, db_item: T) -> T:
        try:
            self.db.commit()
            self.db.refresh(db_item)
            return db_item
        except IntegrityError as e:
            self.db.rollback()
            if 'foreign key constraint' in str(e.orig):
                raise ValueError(f"ForeignKeyViolation: {e.orig}")
            else:
                raise ValueError(f"IntegrityError: {e.orig}")
        except DBAPIError as e:
            self.db.rollback()
            raise ValueError(f"Database error: {str(e.orig)}")

    def get(self, item_id: int) -> T:
        return self.db.query(self.db_model).filter_by(id=item_id).first()

    def create(self, item: CreateSchemaType) -> T:
        db_item = self.db_model(**item.dict())
        self.db.add(db_item)
        return self._execute_with_commit(db_item)

    def update(self, item_id: int, item: CreateSchemaType) -> T:
        db_item = self.get(item_id)
        if db_item:
            for key, value in item.dict().items():
                setattr(db_item, key, value)
            return self._execute_with_commit(db_item)
        raise ValueError(f"Item with id {item_id} not found")

    def partial_update(self, item_id: int, item: UpdateSchemaType) -> T:
        db_item = self.get(item_id)
        if db_item:
            stored_item_dict_copy = db_item.__dict__.copy()
            stored_item_dict_copy.pop('_sa_instance_state', None)
            update_data = item.dict(exclude_unset=True)
            updated_item = {**stored_item_dict_copy, **update_data}
            for key, value in updated_item.items():
                setattr(db_item, key, value)
            return self._execute_with_commit(db_item)
        raise ValueError(f"Item with id {item_id} not found")

    def delete(self, item_id: int) -> None:
        db_item = self.get(item_id)
        if db_item:
            self.db.delete(db_item)
            self.db.commit()
        return db_item
