from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - EID,FULLNAME,JOBTITLE,DEPARTMENT,AGE,GENDER, ETHNICITY, CITY,
    COUNTRY\n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE ;
    \nExample 2 - Tell me all the employee in United States ?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where country ="United States";\nExample 3 - Tell me all the employee whose ethnicity is Asian ?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where ethnicity ="Asian";  
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="Retrieve Data Using SQL query")
st.header("Text To SQL Converter")
st.subheader("Gemini Model Will Convert Text To SQL Query And Fetch The Data From SQLLite DB")
question=st.text_input("Enter text to Query Employee DB: ",key="input")

submit=st.button("Fetch The Data")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"employee.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
