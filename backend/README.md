Run test coverage with command:
docker exec -it <dockercontainer-id> coverage report


 Run tests: 
 docker exec -it <dockercontainer-id> coverage run --source='auth_app' manage.py test auth_app.tests.test_views
