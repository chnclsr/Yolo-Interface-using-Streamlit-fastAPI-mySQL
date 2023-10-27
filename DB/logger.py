class Logger(object):
    def __init__(self, cursor):
        self.cursor = cursor

    def show_databases(self):
        """
        :return: all database names
        """
        self.cursor.execute("SHOW DATABASES")
        print("**" * 25)
        print("---DATABASES---")
        for x in self.cursor:
            print(x)
        print("**" * 25)

    def show_tables(self):
        """
        :return: all tables in the chosen table
        """
        self.cursor.execute("SHOW TABLES")
        print("**" * 25)
        print("---TABLES---")
        for x in self.cursor:
            print(x)
        print("**" * 25)

    def show_table_values(self, tableName: str):
        """
        :return: print all table values in the chosen table
        """
        sql_query = "SELECT * FROM {}".format(tableName)
        self.cursor.execute(sql_query)
        print("**" * 25)
        print("---TABLE VALUES---")
        # get desired info
        result = self.cursor.fetchall()
        # print results
        for row in result:
            print(row)

        print("**" * 25)