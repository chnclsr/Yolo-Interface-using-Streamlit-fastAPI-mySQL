class DataExecuter:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, state=None, tableName=None):
        sql = "INSERT INTO {} (image, time) VALUES (%s, %s)".format(tableName)
        if not isinstance(state, list):
            self.cursor.execute(sql, state)
        else:
            self.cursor.executemany(sql, state)

        print("1 record inserted, ID:", self.cursor.lastrowid)