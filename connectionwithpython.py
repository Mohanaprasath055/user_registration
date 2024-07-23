import mysql.connector
def create_connection():
    return  mysql.connector.connect(host = 'localhost',username = 'root',password = 'Mp!2005',database = 'connectionwithpython')

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    conn.commit()

def insert_user(conn, user_id, name, email):
    cursor = conn.cursor()
    query = f"INSERT INTO users (id,name, email) VALUES ({user_id},'{name}','{email}')"
    cursor.execute(query)
    conn.commit()

def get_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

def id_exists(conn, user_id):
    """Check if a given ID already exists in the users table."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM users WHERE id = {user_id}")
    return cursor.fetchone() is not None

def main():
    conn = create_connection()
    create_table(conn)

    while True:
        user_id = input("Enter ID: ")
        if id_exists(conn, user_id):
            print(f"ID {user_id} already exists. Please enter a different ID.")
            continue
        name = input("Enter name: ")
        email = input("Enter email: ")

        insert_user(conn,user_id, name, email)

        another = input("Do you want to add another user? (yes/no): ")
        if another.lower() != 'yes':
            break

    print("Current users in the database:")
    get_users(conn)
    conn.close()

if __name__ == "__main__":
    main()