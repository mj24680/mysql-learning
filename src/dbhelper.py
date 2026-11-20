import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database= "sql-db")
            self.mycursor = self.conn.cursor()
        except Exception as e:
            print("Some error occurred while connecting to database:", e)
        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute(
                """
                INSERT INTO users (name, email, password) VALUES (%s, %s, %s)
                """, (name, email, password)
            )
            self.conn.commit()
        except:
            return -1
        else:
            1

    def search(self, email, password):

        self.mycursor.execute(
            """
            SELECT * FROM users WHERE email = %s AND password = %s
            """, (email, password)
        )

        data = self.mycursor.fetchall()

        return data