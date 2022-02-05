# **SUMMARY**

This project is used for gaining insights into user activities through sparkify database.
The following were done to achieve this:
i.      Data models were created in sparkifydb(PostgreSQL) using **psycopg2**(a PostgreSQL database adapter for Python programming  language).
ii.     Data from user log and song files are extracted and loaded into the table objects of these created models. 
These dimension tables are songs, artists and users, while the fact table is song_plays
iii.    The time table was loaded from the time extrapolation from the log files that record user activities, which will enable slicing and dicing.


# **INSTRUCTIONS**

1. Open your terminal and navigate to your python environment.
2. Confirm that your python adapter (psycopg2) and pandas. 
3. Navigate to the project directory.
4. Run "python3 create_tables.py" from terminal.
5. Run "python3 etl.py" from terminal.
6. Run test.ipynb on a jupiter notebook to ensure records are inserted into the tables.

# **PROJECT MANIFEST**

- _data_: This directory contains user activity log data and song data in json format.
- _create_tables.py_: python script for creating tables and should be run before running any other script.
- _etl.ipynb_: a python notebook file for practicing data extraction. Codes from this notebook will be transferred to etl.py.
- _etl.py_: is used to extract data from log_data and song_data files and load it into sparkifydb tables
- _README.md_: file is used to show a summary of the project with all its components.
- _sql_queries.py_: python file containing frequently used SQL queries
- _test.ipynb_: notebook file for testing the existence of tables and validating their records.
