import psycopg2
import settings


def connect():
    global connection
    connection = psycopg2.connect(host=settings.db_host, dbname=settings.db_name, user=settings.db_user, password=settings.db_password)

def execute(query):
    global connection
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor

def main():
    print(settings.db_name)

if __name__ == "__main__":
    main()