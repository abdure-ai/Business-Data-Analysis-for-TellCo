import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def connect_to_database():
    """
    Establishes a connection to the PostgreSQL database using .env parameters.

    Returns:
    connection: psycopg2 connection object
    """
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Database connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def fetch_data(conn, query):
    """
    Fetches data from the database using a given query.

    Parameters:
    conn: psycopg2 connection object
    query (str): SQL query to execute

    Returns:
    DataFrame: pandas DataFrame containing the query results
    """
    try:
        df = pd.read_sql_query(query, conn)
        print("Data fetched successfully!")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def close_connection(conn):
    """
    Closes the database connection.

    Parameters:
    conn: psycopg2 connection object
    """
    try:
        conn.close()
        print("Database connection closed!")
    except Exception as e:
        print(f"Error closing connection: {e}")
