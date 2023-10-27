from pydantic import BaseModel

class Settings(BaseModel):
    databaseName: str = "test"  # give a name to the database which will be created
    tableName: str = "requests" # give a name to the table which will be created