import mysql.connector


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(3307)
    )
    return connection


def get_users(query, connection):
    rows = execute_query(query, connection)
    for row in rows:
        print(row)


def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


if __name__ == '__main__':
    conn = connection_database("localhost", "your_username", "your_password", "your_database")
    query = "SELECT * FROM users"
    get_users(query, conn)



