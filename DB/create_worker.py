from .mysqlconnector import *
from .cursor import *
from .tablecreator import *
from .logger import *
from .dataexecuter import DataExecuter
from .tabledropper import *
from .registerdatabase import RegisterDatabase
from .worker import Worker

def create_worker(settings):
    # create a settings object to set all parameters for worker
    db = MySQLConnecter(name=settings.databaseName)
    cursor = Cursor(db)
    logger = Logger(cursor.main_cursor)
    database_creator = DatabaseCreater()
    table_creator = TableCreater()
    table_dropper = TableDropper()
    data_executor = DataExecuter(cursor.main_cursor)
    register_database = RegisterDatabase()
    # create a worker instance which includes all objects respect to \
    # abstraction rule of design pattern
    w_ = Worker(settings,
                    db,
                    cursor,
                    logger,
                    database_creator,
                    table_creator,
                    table_dropper,
                    data_executor,
                    register_database)
    return w_