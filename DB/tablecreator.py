class TableCreater(object):
    @staticmethod
    def create_table(cursor, table_name, params):
        cursor.execute("CREATE TABLE IF NOT EXISTS {} {}".format(table_name, params))


class DatabaseCreater(object):
    @staticmethod
    def create_database(cursor, database_name: str):
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
