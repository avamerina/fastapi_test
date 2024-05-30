from typing import Generic, TypeVar
from fastapi import HTTPException
from app.repositories.base_crud import BaseCRUD

T = TypeVar('T')
CreateSchemaType = TypeVar('CreateSchemaType')
UpdateSchemaType = TypeVar('UpdateSchemaType')


class BaseService(Generic[T, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, repository: BaseCRUD[T, CreateSchemaType, UpdateSchemaType]) -> None:
        self.repository = repository

    def get(self, item_id: int) -> T:
        item = self.repository.get(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    def create(self, item: CreateSchemaType) -> T:
        return self.repository.create(item)

    def update(self, item_id: int, item: CreateSchemaType) -> T:
        db_item = self.repository.get(item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return self.repository.update(item_id, item)

    def partial_update(self, item_id: int, item: UpdateSchemaType) -> T:
        db_item = self.repository.get(item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return self.repository.partial_update(item_id, item)

    def delete(self, item_id: int) -> None:
        db_item = self.repository.get(item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        self.repository.delete(item_id)
