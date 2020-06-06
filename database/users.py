from .connection import with_connection

@with_connection
def addUser(connection, username, password, fullName):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (%s,%s,%s);", (username, password, fullName))

@with_connection
def updateUser(connection, username, password, fullName):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET password = %s, full_name = %s WHERE username = %s", (password, fullName, username))
    pass

@with_connection
def deleteUser(connection, username):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username = %s", (username,))

@with_connection
def listUsers(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users ORDER BY username;")
    return cursor.fetchall()

@with_connection
def userExists(connection, username):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    return cursor.rowcount