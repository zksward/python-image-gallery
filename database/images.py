from .connection import with_connection

@with_connection
def addImage(connection, username, s3_key):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO images(user_id, s3_key) SELECT id, %s FROM users WHERE username = %s;", (s3_key, username))

@with_connection
def deleteImage(connection, username, image_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM images WHERE image_id = %s AND user_id = (SELECT id FROM users WHERE username = %s);", (image_id, username))

@with_connection
def listImages(connection, username):
    cursor = connection.cursor()
    cursor.execute("SELECT i.id, i.user_id, i.s3_key FROM images i INNER JOIN users u on u.id = i.user_id WHERE u.username = %s;", (username,))
    return list(map(imageDict, cursor.fetchall()))

@with_connection
def getImage(connection, username, image_id):
    cursor = connection.cursor()
    cursor.execute("SELECT i.id, i.user_id, i.s3_key FROM images i INNER JOIN users u on u.id = i.user_id WHERE u.username = %s AND i.image_id = %s;", (username, image_id))
    if cursor.rowcount > 0:
        return imageDict(cursor.fetchone())
    else:
        return None

@with_connection
def imageExists(connection, username, image_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM images WHERE id = %s AND user_id = (SELECT id FROM users WHERE username = %s);", (image_id, username))
    return cursor.rowcount

def imageDict(image):
    keys = ('id', 'user_id', 's3_key')
    return {keys[i] : image[i] for i, _ in enumerate(image)}