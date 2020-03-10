1- setting up models

2- API

POST teacher
curl -X POST -H "Content-Type: application/json" -d '{"name": "omar"}' http://127.0.0.1:5000/teachers

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
