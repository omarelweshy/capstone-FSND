#### School Capstone Project 

### Motivation
Welcome To our School :))
This Project is for Get data for your school, Get Teachers, Students Create, Delete and Update ...etc.
In Project you can stucture your data of school and make roles which allow you to control your permissions of users.
From a technical side :
    - Project have tests to ensure from endpoints
    - Authentication system
and more :)))
Now you can explore
I hope you like the project :)
Let's EXPLORE !! 

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

Response :
{
    "status_code": 200,
    "success": true
}
--------------------------------------------------

POST student
- Posting a student
- Take student name and return success 

Run `curl -X POST -H "Content-Type: application/json" -d '{"name": "Name Here"}' http://127.0.0.1:5000/students`

Response :
{
    "status_code": 200,
    "success": true
}
--------------------------------------------------

GET teachers
- Get all teachers names

Run `curl -X GET http://127.0.0.1:5000/teachers`

Response :
{
    "status_code": 200,
    "success": true,
    "tearcher": {
        "1": "omar",
        "2": "Any name",
        "3": "omar",
        "4": "Anas",
        "5": "Any name",
    }
}
--------------------------------------------------

GET students
- Get all students names
Run `curl -X GET http://127.0.0.1:5000/students`
Response :
{
    "status_code": 200,
    "success": true,
    "tearcher": {
        "1": "joe",
        "2": "Anas",
        "3": "omar",
        "4": "Messi",
    }
}
-------------------------------------------------

DELETE teacher
- Delete teacher by id
- Take id and return success

Run `curl -X DELETE http://127.0.0.1:5000/teachers/1`

Response :
{
    "status_code": 200,
    "success": true
}
-------------------------------------------------

DELETE student
- Delete student by id
- Take id and return success 
Run `curl -X DELETE http://127.0.0.1:5000/students/1`

Response :
{
    "status_code": 200,
    "success": true
}
-------------------------------------------------

PATCH teacher
- Take data and id of teacher
- Return success and patch teacher

Run `curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Something else"}' http://127.0.0.1:5000/teachers/1`

Response :
{
    "status_code": 200,
    "success": true
}
-------------------------------------------------

PATCH student
- Take data and id of teacher
- Return success and patch student
Run `curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Something else"}' http://127.0.0.1:5000/students/1`

Response :
{
    "status_code": 200,
    "success": true
}

### AUTHENTCATION

AUTH0_DOMAIN = 'omarcap.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'school'
CLIENT_ID = '84fHKL9mXnvUFv2j0YKxtPtdMR5Ehs4I'
redirect_uri= `http://127.0.0.1:5000/result`

you can sign in with link and get access token from link
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

Errors are returned as JSON objects from endpoints fail in the following format:
# 400
{
    "success": False, 
    "error": , 400
    "message": "bad request"
}

# 405
{
    "success": False,
    "error": 405,
    "message": "Method not allow"
}

# 422
{
    "success": False,
    "error": 422,
    "message": "unprocessable"
}

# 404
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}


## Testing
To run the tests, run
```
dropdb school_test
createdb school_test
python test_flaskr.py
```

### APP URL HEROK
`https://omarschool.herokuapp.com/`