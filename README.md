A Python-based chat assistant that translates natural language queries into SQL queries and fetches relevant data from an SQLite database.

🛠 Features
✅ Converts English queries into SQL commands
✅ Retrieves employee & department data from an SQLite database
✅ Handles invalid queries & incorrect department names gracefully
✅ Uses Google Gemini AI for query generation
✅ Built with Streamlit for an interactive UI

📌 Supported Queries
The assistant supports a variety of SQL-based queries, such as:
✔️ Show me all employees in the [department] department.
✔️ Who is the manager of the [department] department?
✔️ List all employees hired after [date].
✔️ What is the total salary expense for the [department] department?
✔️ More complex queries related to employees & departments.

⚙️ Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/AI-Powered-SQL-Assistant.git
cd AI-Powered-SQL-Assistant
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv  
source venv/bin/activate  # On Mac/Linux  
venv\Scripts\activate  # On Windows  
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root and add:

makefile
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key
🚀 Running the Application
Run the Streamlit app using:

bash
Copy
Edit
streamlit run app.py
This will launch the app in your web browser. 🎉

🗂 Database Schema
The SQLite database Employees.db contains two tables:

EMPLOYEES Table
Column	Type	Description
ID	INT (PK)	Unique employee ID
Name	VARCHAR(25)	Employee name
Department	VARCHAR(20)	Employee's department
Salary	DECIMAL(10,2)	Employee's salary
Hire_Date	DATE	Hiring date
DEPARTMENTS Table
Column	Type	Description
ID	INT (PK)	Unique department ID
Name	VARCHAR(25)	Department name
Manager	VARCHAR(25)	Department manager
The tables are connected by EMPLOYEES.Department → DEPARTMENTS.Name.

🛠 Technologies Used
Python 🐍
Streamlit 🎨 (Frontend)
SQLite 🗄️ (Database)
Google Gemini AI 🤖 (Natural Language to SQL conversion)
🛡️ Error Handling
✅ Gracefully handles invalid SQL queries
✅ Returns meaningful messages for incorrect department names
✅ Prevents SQL injection risks

📜 License
This project is open-source under the MIT License.

🤝 Contributing
Feel free to submit pull requests or open issues for improvements! 🚀
