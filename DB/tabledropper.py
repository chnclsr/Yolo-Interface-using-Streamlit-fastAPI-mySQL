class TableDropper(object):
    @staticmethod
    def drop_table(cursor, database_name, table_name: str):
        cursor.execute("DROP TABLE IF EXISTS {};".format(table_name))