from create_worker import create_worker
from tablecolumnskeygenerator import TableColumnsKeyGenerator
from settings import Settings

if __name__ == '__main__':
    settings = Settings()
    # create an object to generate a table column keys and their datatypes
    params_generator = TableColumnsKeyGenerator()
    worker = create_worker(settings)


    columns_keys = \
        [
        "image VARCHAR(255)",
        "time VARCHAR(255)"
        ]

    # get prompts with given keys and values to create table
    prompt4create_specific_table = params_generator.create_params_prompt(columns_keys)

    worker.create_specific_db()
    worker.drop_table_from_chosen_db()
    worker.create_specific_table_in_chosen_db(prompt4create_specific_table)

    val = ("cihan", "paris")
    # add columns to the table which I want
    # val = [
    #     ('cihan',   'Lowstreet 4'),
    #     ('Amy',     'Apple st 652'),
    #     ('Hannah',  'Mountain 21'),
    #     ('Michael', 'Valley 345'),
    #     ('Sandy',   'Ocean blvd 2'),
    #     ('Betty',   'Green Grass 1'),
    #     ('Richard', 'Sky st 331'),
    #     ('Susan',   'One way 98'),
    #     ('Vicky',   'Yellow Garden 2'),
    #     ('Ben',     'Park Lane 38'),
    #     ('William', 'Central st 954'),
    #     ('Chuck',   'Main Road 989'),
    #     ('Viola',   'Sideway 1633')
    # ]

    worker.add_values2chosen_db(val)

    worker.logger.show_databases()
    worker.logger.show_tables()
    worker.logger.show_table_values(tableName=settings.tableName)



