import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = conn.cursor()

        # Retrieve states sorted by states.id in ascending order
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Display results
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close connections
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
    else:
        print("Usage: python script.py <username> <password> <database_name>")

