import mariadb

# database connection params
def db_driver():
    try:
        conn = mariadb.connect(
            user="taha",
            password="password1",
            host="192.168.0.4",
            port=3306,
            database="miniHR"

        )
    except mariadb.Error as e:
        return None
    return conn
