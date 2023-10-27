import mysql.connector

class MySQLConnecter(object):
    def __init__(self, name=None):
        self.db = None
        self.connect(name)

    def connect(self, name=None):
        if name is not None:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="877611"
            )
        else:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="877611",
                database=name
            )

    def update(self):
        self.db.commit()






