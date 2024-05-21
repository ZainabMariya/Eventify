import psycopg2
import os 

def create_database(user, pw):
    """
    Creates the EVENTIFY database
    """
    try:
        conn = psycopg2.connect(
            dbname = 'postgres',  
            user = user,
            password = pw,
            host = 'localhost',
            port = '5432'
        )
        print('Connection to postgres: Successful')
        conn.autocommit = True

        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE EVENTIFY")

        print("Database created successfully!")

    except psycopg2.Error as e:
        print(f'Error: {e}')
    finally:
        if conn is not None:
            conn.close()

def get_query(file_path):
    """
    Gets the SQL query from a text file
    """
    with open(file_path, 'r') as f:
        queries = f.read()
    
    return queries


try:
    username = 'mariyamohiuddin'
    # input('Enter username: ')
    password = 'Zamamo25803'
    # input('Enter password: ')
    create_database(username, password)


    conn = psycopg2.connect(dbname = 'eventify',
                            user = username,
                            password = password,
                            host = 'localhost',
                            port = 5432)
    print('Connection to EVENTIFY_DATABASE: Success')
    conn.autocommit = True

    cursor = conn.cursor()
    create_file_path = os.getcwd() + '/sql/create_queries.sql'
    insert_file_path = os.getcwd() + '/sql/insert_queries.sql'
    files = [create_file_path, insert_file_path]
    for file in files:
        queries = get_query(file)
        cursor.execute(queries)
        if file == create_file_path:
            print('Tables created!')
        else:
            print('Data inserted!')
except psycopg2.Error as error:
    print(f'Error: {error}')