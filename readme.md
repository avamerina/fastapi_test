## Prerequisites

Make sure you have the following installed:

```
Docker
Docker Compose
```

## Installation

Clone the repository:

```
git clone https://github.com/your-repo.git
cd your-repo
```

Create a .env file in the project root directory and add the following environment variables:

```
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
```

## Running the Project

Build and start the Docker containers:

```
docker-compose up --build
```

The FastAPI application will be available at http://localhost:8000.

## API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

```
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
```

## API Endpoints

Students

```
GET /students/{student_id}

POST /students/

PUT /students/{student_id}/

PATCH /students/{student_id}/

DELETE /students/{student_id}/
```


Scores

```
GET /scores/{score_id}

POST /scores/

PUT /scores/{score_id}/

PATCH /scores/{score_id}/

DELETE /scores/{score_id}/
```

## Testing

To test the API endpoints, you can use tools like curl, Postman, or the interactive API documentation provided by FastAPI.

Example curl commands:

```
curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20}'

curl -X GET "http://localhost:8000/students/1"

curl -X PUT "http://localhost:8000/students/1/" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "age": 21}'

curl -X DELETE "http://localhost:8000/students/1/"
```


