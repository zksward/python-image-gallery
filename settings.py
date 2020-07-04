import os

db_host = os.getenv("PG_HOST")
db_name = os.getenv("IG_DATABASE")
db_user = os.getenv("IG_USER")
if os.getenv("IG_PASSWD_FILE") is None:
    db_password = os.getenv("IG_PASSWD")
else:
    with open(os.getenv("IG_PASSWD_FILE"), 'r') as file:
        db_password = file.read().replace('\n', '')