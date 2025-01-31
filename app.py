import streamlit as st # type: ignore
import os
import sqlite3
from dotenv import load_dotenv # type: ignore
import google.generativeai as genai # type: ignore

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get SQL query from Gemini AI
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])

    # Clean up the response: remove markdown formatting, extra spaces, and newlines
    clean_query = response.text.replace("```sql", "").replace("```", "").strip()
    return clean_query

# Function to execute SQL query safely
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        # Execute query
        cur.execute(sql)
        rows = cur.fetchall()

        conn.commit()
        conn.close()

        # If no results found, return a meaningful message
        if not rows:
            return [("No results found. Please check the department name or query.",)]

        return rows
    except Exception as e:
        return [(f"Error executing query: {str(e)}",)]

# Defining Prompt
prompt = [
    """
    You are an expert in converting English questions into SQL queries!
    
    The SQL database 'Employees' has two tables:
    
    1. **EMPLOYEES** table with the following columns:
       - ID (Primary Key)
       - Name
       - Department (Foreign Key referencing DEPARTMENTS.Name)
       - Salary
       - Hire_Date
    
    2. **DEPARTMENTS** table with the following columns:
       - ID (Primary Key)
       - Name (Unique, references EMPLOYEES.Department)
       - Manager
    
    These two tables are connected via the `Department` column in the EMPLOYEES table,  
    which references the `Name` column in the DEPARTMENTS table.
    
    **Examples:**
    
    - **Example 1:**  
      **Question:** Show me all employees in the Sales department.  
      **SQL Query:**  
      SELECT Name FROM EMPLOYEES WHERE Department = 'Sales';
    
    - **Example 2:**  
      **Question:** Who is the manager of the Marketing department?  
      **SQL Query:**  
      SELECT Manager FROM DEPARTMENTS WHERE Name = 'Marketing';
    
    **Instructions:**  
    - Generate only the SQL query as output, without any additional text or formatting.  
    - Do NOT include triple quotes (`'''`) or markdown code blocks (```sql ... ```).  
    - Ensure that invalid queries or department names return "No results found."
    """
]

# Streamlit App
st.set_page_config(page_title="SQL Query Chatbot")
st.header("💬 AI-Powered SQL Assistant")

# User Input
question = st.text_input("Enter your question: ", key="input")

# Submit Button
submit = st.button("Ask the question")

# If button is clicked
if submit:
    response = get_gemini_response(question, prompt)

    # Debugging - Print the generated SQL query
    #print("Generated SQL Query:", response)

    # Execute SQL query
    data = read_sql_query(response, "Employees.db")

    # Display the response
    st.subheader("🔍 Query Result:")
    for row in data:
        st.write(row[0])  # Display result properly
