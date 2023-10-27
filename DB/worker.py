

class Worker(object):
    def __init__(self, settings,
                 db,
                 crsr,
                 logger,
                 database_creator,
                 table_creator,
                 table_dropper,
                 data_executor,
                 register_database):
        self.settings = settings
        self.db = db
        self.crsr = crsr
        self.logger = logger
        self.specific_databaseCreator = database_creator
        self.specific_tableCreator = table_creator
        self.specific_tableDropper = table_dropper
        self.data_executer = data_executor
        self.register_database = register_database
        self.request_counter = 0


    def create_specific_table_in_chosen_db(self, params):
        self.register2chosen_db()
        self.specific_tableCreator.create_table(cursor=self.crsr.main_cursor,
                                                  table_name=self.settings.tableName,
                                                  params=params)
    def create_specific_db(self):
        # create a database with the specified name
        self.specific_databaseCreator.create_database(cursor=self.crsr.main_cursor,
                                                    database_name=self.settings.databaseName)

    def register2chosen_db(self):
        self.register_database.register_database(cursor=self.crsr.main_cursor,
                                                 database_name=self.settings.databaseName)

    def drop_table_from_chosen_db(self):
        self.register2chosen_db()
        self.specific_tableDropper.drop_table(cursor=self.crsr.main_cursor,
                                              database_name=self.settings.databaseName,
                                              table_name=self.settings.tableName)
        self.update_chosen_db()

    def update_chosen_db(self):
        self.db.update()

    def add_values2chosen_db(self, values):
        self.data_executer.execute(state=values, tableName=self.settings.tableName)
        self.update_chosen_db()
        self.request_counter += 1



