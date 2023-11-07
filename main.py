import time
import torch
from app import App
from DB.create_worker import create_worker
from DB.tablecolumnskeygenerator import TableColumnsKeyGenerator
from DB.settings import Settings
import streamlit as st
from DB.dataloader import DataLoader
from logallcommand import LogAllCommand
from client import HttpClient

st.set_page_config(layout="wide")


def main():
    # Keys for database columns
    columns_keys = [
        "image VARCHAR(255)",
        "time VARCHAR(255)"
    ]

    ### ----------------   MySQL Database ---------------- ###
    # Create settings object
    settings = Settings()

    # Create an object to generate table column keys and their data types
    params_generator = TableColumnsKeyGenerator()

    # Create a worker to perform database operations
    worker = create_worker(settings)

    # Get prompts with given keys and values to create a table
    prompt4create_specific_table = params_generator.create_params_prompt(columns_keys)

    # Create a specific database to collect responses' information
    worker.create_specific_db()

    # Drop the table if it exists in the chosen database
    worker.drop_table_from_chosen_db()

    # Wait until the table is dropped
    time.sleep(3)

    # Create a specific table in the chosen database using the prompts
    worker.create_specific_table_in_chosen_db(prompt4create_specific_table)

    ### ----------------   Dataloader ---------------- ###
    # Create a data loader
    data_loader = DataLoader()

    # Make specific video loader
    data_loader.set_video_loader()

    # Create an HTTP client
    httpclient = HttpClient()

    ### ----------------   Streamlit app ---------------- ###
    # Create an instance of the application
    app = App(st, worker, data_loader, LogAllCommand(st, data_loader))

    # Set http client
    app.set_http_client(httpclient)

    # Set the title and sidebar title
    app.st.title("Object Recognition Dashboard")
    app.st.sidebar.title("Settings")

    # Device options
    if torch.cuda.is_available():
        device_option = app.st.sidebar.radio("Select Device", ['cpu', 'cuda'], disabled=False, index=0)
    else:
        device_option = app.st.sidebar.radio("Select Device", ['cpu', 'cuda'], disabled=False, index=0)

    # Change the selected device
    app.changeDevice(device_option)

    # Add a separator in the sidebar
    app.st.sidebar.markdown("---")

    # Start the video processing function
    app.process_video()



if __name__ == "__main__":
    main()