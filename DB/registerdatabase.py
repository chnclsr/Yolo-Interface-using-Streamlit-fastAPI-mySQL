class RegisterDatabase(object):
    @staticmethod
    def register_database(cursor, database_name):
        cursor.execute("USE %s" % database_name)