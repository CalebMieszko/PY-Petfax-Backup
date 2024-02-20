import psycopg2

try:
    conn = psycopg2.connect(
        dbname='petfax',
        user='postgres',  # Replace with your username
        password='D#V0luti0n',  # Replace with your password
        host='localhost',
        port='5433'
    )
    print("Connected to the database successfully")
except Exception as e:
    print("Unable to connect to the database:")
    print(e)
