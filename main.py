import time
import torch
from app import App
from DB.create_worker import create_worker
from DB.tablecolumnskeygenerator import TableColumnsKeyGenerator
from DB.settings import Settings
import streamlit as st
from DB.dataloader import DataLoader
from logallcommand import LogAllCommand
from httpclient import HttpClient

st.set_page_config(layout="wide")


def main():
    columns_keys = \
        [
        "image VARCHAR(255)",
        "time VARCHAR(255)"
        ]
    settings = Settings()
    # create an object to generate a table column keys and their datatypes
    params_generator = TableColumnsKeyGenerator()
    worker = create_worker(settings)

    # get prompts with given keys and values to create table
    prompt4create_specific_table = params_generator.create_params_prompt(columns_keys)

    # create specific database to collect responses' information
    worker.create_specific_db()

    # drop table if it exists in chosen database
    worker.drop_table_from_chosen_db()

    # wait until table is dropped
    time.sleep(3)
    worker.create_specific_table_in_chosen_db(prompt4create_specific_table)

    data_loader = DataLoader()
    data_loader.getVideoLoader()

    httpclient = HttpClient()
    app = App(st, worker, data_loader, LogAllCommand(st, data_loader))
    app.set_http_client(httpclient)
    app.st.title("Object Recognition Dashboard")
    app.st.sidebar.title("Settings")

    # device options
    if torch.cuda.is_available():
        device_option = app.st.sidebar.radio("Select Device", ['cpu', 'cuda'], disabled=False, index=0)
    else:
        device_option = app.st.sidebar.radio("Select Device", ['cpu', 'cuda'], disabled=False, index=0)

    app.changeDevice(device_option)

    app.st.sidebar.markdown("---")



    app.process_video()


if __name__ == "__main__":
    main()