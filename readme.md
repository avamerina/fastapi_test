Prerequisites
Make sure you have the following installed:

Docker
Docker Compose


Installation
Clone the repository:

git clone https://github.com/your-repo.git
cd your-repo
Create a .env file in the project root directory and add the following environment variables:


POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db

Running the Project
Build and start the Docker containers:

docker-compose up --build
The FastAPI application will be available at http://localhost:8000.

API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

API Endpoints

Students

Get Student by ID
GET /students/{student_id}

Create Student
POST /students/

Update Student
PUT /students/{student_id}/

Partial Update Student
PATCH /students/{student_id}/

Delete Student
DELETE /students/{student_id}/

Scores

Get Score by ID
GET /scores/{score_id}

Create Score
POST /scores/

Update Score
PUT /scores/{score_id}/

Partial Update Score
PATCH /scores/{score_id}/

Delete Score
DELETE /scores/{score_id}/

Testing
To test the API endpoints, you can use tools like curl, Postman, or the interactive API documentation provided by FastAPI.

Example curl commands:

Create a student:
curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20}'

Get a student:
curl -X GET "http://localhost:8000/students/1"

Update a student:
curl -X PUT "http://localhost:8000/students/1/" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "age": 21}'


Delete a student:
curl -X DELETE "http://localhost:8000/students/1/"


