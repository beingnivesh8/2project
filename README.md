# 2project
PHONEPE PULSE DATA VISUALIZATION AND EXPLORATION : A USER FRIENDLY TOOL USING STREAMLIT AND PLOTLY

This project aims to develop a user-friendly Streamlit application that utilizes PhonePe Pulse dataset using Git cloning to extract information, stores it in a SQL database and enable the users to get geoplots and other visualization elements for enhanced data exploration and insights in the Streamlit app.

# INTRODUCTION:

PhonePe is a popular digital payments platform in India, offering a range of financial services through its mobile app. Users can make payments, transfer money, recharge phones, pay bills, invest, shop online, and more.
PhonePe has become a preferred choice for millions of users, contributing to India's digital payments revolution.

# FILES:

(1)ipynb file;
 
   It involves cloning the PhonePe Pulse dataset using Git then transforming the data into dataframe by using Pandas. The transformed data is subsequently stored in a SQL database with help of SQL conncetor and SQL-Alchemy engine. Additionally, an interactive dashboard is developed with Streamlit and Plotly, featuring geoplots and other visualization elements for enhanced data exploration and insights.

(2)py file;

  It involves Creating an interactive dashboard with Streamlit and Plotly, featuring geoplots and other visualization elements for enhanced data exploration, insights and also having Queries and answers.

# ESSENTIAL LIBRARIES:

import os, 
import json, 
import git, 
import pandas as pd, 
import plotly.express as px, 
import streamlit as st, 
from streamlit_option_menu import option_menu, 
import time, 
import mysql.connector and  
from sqlalchemy import create_engine.

# DATA SOURCE:

The data utilized in this project predominantly consists of openly available datasets sourced from PhonePe - https://github.com/PhonePe/pulse

# WORK FLOW:

This project Clones the Git repository, processes the data, and stores it in the MYSQL database. It has the option to migrate the data to MySQL using SQLAlchemy then analyse the data and featuring geoplots and other visualization elements for enhanced data exploration, insights and also having Queries and answers in the streamlit. 
The step by step procedures are shown below;

STEP 1 : The data is extracted from the PhonePe Pulse GitHub repository and cloned to the local environment, ensuring access to the latest dataset for analysis.

STEP 2 : The raw data undergoes transformation, including cleaning, formatting, and structuring in dataframe format using pandas

STEP 3 : Mysql connector used for connection between Python and MySQL database, enabling data transfer. SQLAlchemy's engine facilitates efficient data insertion and querying, simplifying 
         database interactions for Python.
        
STEP 4 : With the assistance of Streamlit and Plotly, a dashboard and charts are created, offering geospatial visualizations, top insights and also Query details. This setup empowers 
         users to explore and reveal trends within the dataset, facilitating insightful analysis.

# LESSONS LEARNED:

Git Cloning, Python scripting, Data Collection, Data Management using SQL, Streamlit and Plotly.

# LINK:

http://localhost:8501
