# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:19:02 2020

@author: aakas
"""

# Purpose of this file is to pull data from RDS Postgres DB Instance which hosts our S3 object

# Importing Reuqired Modules
import psycopg2
import pandas as pd

# Connect to the PostgreSQL database
conn = psycopg2.connect(host="#################################################",
                        database="", user="#########", password="##########")
# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def create_pandas_table(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table
  
# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable
df = create_pandas_table("SELECT * FROM Retail")
df

books = create_pandas_table("SELECT * FROM books")
books

users = create_pandas_table("SELECT * FROM users")
users

ratings = create_pandas_table("SELECT * FROM Ratings")
ratings

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()


# Creating a function to pass the data to Jupyter Notebook for further analysis
def get_books_data():
    """
    
    return: dataframe pulled from Postgres Database
    """
    data_books = books
    return data_books

 def get_ratings_data():
 	data_ratings = ratings
 	return data_ratings

 def get_users_data():
 	data_users = users
 	return data_users