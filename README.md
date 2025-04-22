1. We merged the arc_refactor to master 
2. We installed psycopg2-binary
    `pipenv install psycopg2-binary`
3. Start the application and check if everything runs well
4. Migrate all the endpoints to a HTTP client to be able to test it when needed (Insomnia, Postman)
5. Create a db.py app
    - create a function get_db() that rerurns the connection, also use the g object from flask
    - create a close_db function that will be trigerred everytime the teadown of the flask app is happening automatically
6. Create a db_init file that creates the needed tables
7. Create the additional layer that will handle db interactions (repository layer)
