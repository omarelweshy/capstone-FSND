#### School Capstone Project 
This project is for save data for a school

#### Getting Started
Firstly, you should have python3 and as a recommend you can install Virtual Enviornment

### Install requirements
you can install requirements to run project
bash
`pip3 install -r requirements.txt` you may use `pip` or `pip3`

### Run server
To run server :
    - Define app in dir `export FLASK_APP=app.py;`
    - Run flask with reload to reload when you change any thig `flask run --reload`

### Setup database
Just create Postgresql DB and run the application to make migrations

### API define
In project 2 POST, 2 GET, 2 PATCH, 2 DELETE requests 

You can use postman to run APIs or command line

POST teacher
- Posting a teacher
- Take teacher name and return success 

Run `curl -X POST -H "Content-Type: application/json" -d '{"name": "Name Here"}' http://127.0.0.1:5000/teachers`


POST student

`curl -X POST -H "Content-Type: application/json" -d '{"name": "omar"}' http://127.0.0.1:5000/students`

GET teachers
curl -X GET http://127.0.0.1:5000/teachers

GET students
curl -X GET http://127.0.0.1:5000/students

DELETE teacher
curl -X DELETE http://127.0.0.1:5000/teachers/1

DELETE student
curl -X DELETE http://127.0.0.1:5000/students/1

PATCH teacher
curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Something else"}' http://127.0.0.1:5000/teachers/4

PATCH student
curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Something else"}' http://127.0.0.1:5000/students/2

### AUTHENTCATION

AUTH0_DOMAIN = 'omarcap.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'school'
CLIENT_ID = '84fHKL9mXnvUFv2j0YKxtPtdMR5Ehs4I'
redirect_uri= `http://127.0.0.1:5000/result`

you can sign in with link and get access token form link
`https://omarcap.auth0.com/authorize?audience=school&response_type=token&client_id=84fHKL9mXnvUFv2j0YKxtPtdMR5Ehs4I&redirect_uri=http://127.0.0.1:5000/result`

We have two roles
- Manager
Manager can:
    - `get:teachers	`
    - `get:students`
    - `post:teachers`
    - `post:students`
    - `delete:teachers`
    - `delete:students`
    - `patch:teachers`
    - `patch:students`
Manager Account
user : admin@admin.com
password : Aa12345678900..

- Teacher
Teacher can:
    - `get:teachers	`
    - `get:students`
    - `post:students`
    - `delete:students`
    - `patch:students`
Teacher Account
user : teacher@teacher.com
password : Aa12345678900..


## Errors handling:

Errors are returned as JSON objects in the following format:
{
    "success": False, 
    "error": , 400
    "message": "bad request"
}
The API will return three error types when requests fail:

400: Bad Request
404: Resource Not Found
422: unprocessable


## Testing
To run the tests, run
```
dropdb school_test
createdb school_test
python test_flaskr.py
```