import psycopg2
import settings

connection = None

# https://www.psycopg.org/articles/2010/10/22/passing-connections-functions-using-decorator/
def with_connection(function):
    def with_connection_(*args, **kwargs):
        global connection
        if not connection:
            secret = settings.get_database_secret()
            connection = psycopg2.connect(host=secret['host'], dbname=secret['dbname'], user=secret['username'], password=secret['password'])
        try:
            result = function(connection, *args, **kwargs)
        except Exception:
            connection = None
            raise
        else:
            connection.commit()

        return result

    return with_connection_