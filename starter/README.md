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
curl -X POST -H "Content-Type: application/json" -d '{"name": "omar"}' http://127.0.0.1:5000/students

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
CLIENT_DI = '84fHKL9mXnvUFv2j0YKxtPtdMR5Ehs4I'
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
JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VRkVSVVl4UTBFNFFUY3lSRGd4UkRrd01qRXdNemhHUVRGQ1JVRkdNRU13UkRFek1qUTROZyJ9.eyJpc3MiOiJodHRwczovL29tYXJjYXAuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNjc3YjlhNjBhY2FhMGQ3ZGVhYzY4NyIsImF1ZCI6InNjaG9vbCIsImlhdCI6MTU4Mzg0MTE3OSwiZXhwIjoxNTgzODQ4Mzc5LCJhenAiOiI4NGZIS0w5bVhudlVGdjJqMFlLeHRQdGRNUjVFaHM0SSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnN0dWRlbnRzIiwiZGVsZXRlOnRlYWNoZXJzIiwiZ2V0OnN0dWRlbnRzIiwiZ2V0OnRlYWNoZXJzIiwicGF0Y2g6c3R1ZGVudHMiLCJwYXRjaDp0ZWFjaGVycyIsInBvc3Q6c3R1ZGVudHMiLCJwb3N0OnRlYWNoZXJzIl19.B1oINPdPDQtczZ1I-wE-QstH9asjPMER4utg9BZq3d9jQzbh-n6DhBZQ15kVZCSlyT26ur0qS_MjbUn-WdBoSorGtVeNNfg9XlLsMXB1Ad4JscRj_H8658DQXEujAplBpxWavNC-Bld07ocTiJ_SV-TADDAdkccFqrz-aiNeJyPFS9Kk6ircWKZz6Nn_b-Tus_p_UkTC2TZOO10drwPbexroNzP1FBb1P8yHoJPdrQzYq6P1IVa1FugkmDZvU7i6Hvk4AO2EVc7SKZcE0i8kKN6hwDfzJqjiIFbM1NMzFFd1FMhKjXBTdUJcJVjK3vA128HdXlT33F6NxuzMFmDlhg`


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
JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VRkVSVVl4UTBFNFFUY3lSRGd4UkRrd01qRXdNemhHUVRGQ1JVRkdNRU13UkRFek1qUTROZyJ9.eyJpc3MiOiJodHRwczovL29tYXJjYXAuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNjc3YmU4YTViMDk0MGRjNjlmZjI5MyIsImF1ZCI6InNjaG9vbCIsImlhdCI6MTU4Mzg0MTMwNSwiZXhwIjoxNTgzODQ4NTA1LCJhenAiOiI4NGZIS0w5bVhudlVGdjJqMFlLeHRQdGRNUjVFaHM0SSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnN0dWRlbnRzIiwiZ2V0OnN0dWRlbnRzIiwiZ2V0OnRlYWNoZXJzIiwicGF0Y2g6c3R1ZGVudHMiLCJwb3N0OnN0dWRlbnRzIl19.xizzi4tMvay4ooW-o67iCQL7svtM9vsD9wwZykDQNFInO6bjDsVhoIBoieuy0cWHr9a3tIwf5Aidaj7l4QzQtEFI3-L6e-5s6GKPJx907gOM9MrJ_shXfuuybGJalJ6JT02iuliNyhKtIqOrsb1YS7-KcOY72Ub0V1tyiO5_FXDeixRcR-qn93QomfuvhYe8RulHGHaLbN2XcF9U4M2zNxrUlJNVJyoyOh05xNFoTjSF3NtbLXoGfQf6_4aWeQysUyMZ4ykBFzyfGZWLcx4HuljSMIJmTGG7dLVQnHj_E70k1blX6k0kY3LAS1sOiU9URMM6NkKKsQDc11B0By4NgA`




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