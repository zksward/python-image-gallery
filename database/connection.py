import psycopg2
import settings

connection = None

# https://www.psycopg.org/articles/2010/10/22/passing-connections-functions-using-decorator/
def with_connection(function):
    def with_connection_(*args, **kwargs):
        global connection
        if not connection:
            connection = psycopg2.connect(host=settings.db_host, dbname=settings.db_name, user=settings.db_user, password=settings.db_password)
        try:
            result = function(connection, *args, **kwargs)
        except Exception:
            connection = None
            raise
        else:
            connection.commit()

        return result

    return with_connection_