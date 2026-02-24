📊 Spreadsheet to PostgreSQL Converter

A Python-based utility that allows users to import CSV or Excel files into a PostgreSQL database automatically.

This tool dynamically:

Reads spreadsheet files

Infers column names

Infers data types

Creates database tables

Inserts data into PostgreSQL

All with minimal user effort.

🚀 Why This Project?

Manually creating tables and inserting spreadsheet data into databases is:

time-consuming

error-prone

repetitive

This project automates that process while keeping the logic transparent, extensible, and beginner-friendly.

🧠 What This Project Does

Takes a .csv or .xlsx file

Reads headers and rows

Infers PostgreSQL data types (INTEGER, NUMERIC, TEXT)

Creates a table if it does not exist

Inserts all rows safely into PostgreSQL

🛠️ Tech Stack

Python

PostgreSQL

psycopg2

openpyxl

📁 Project Structure
.
├── main.py                    # Entry point
├── import_spreadsheet_file.py # Handles CSV / Excel reading
├── convert_to_database.py     # PostgreSQL logic
├── requirements.txt
├── README.md
✅ Prerequisites

Before running the project, make sure you have:

Python 3.10+

PostgreSQL installed and running

A PostgreSQL database already created

⚠️ This tool does NOT create the database itself — only tables inside it.

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/fahad15fede/data-importer-to-pgsql.git
cd data-importer-to-pgsql
2️⃣ Create and activate virtual environment
python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ How to Use
1️⃣ Prepare your spreadsheet

File must be .csv or .xlsx

First row must contain column headers

Data should be clean and consistent

2️⃣ Create a PostgreSQL database manually

Example:

CREATE DATABASE my_database;
3️⃣ Run the program
python main.py
4️⃣ Enter required details when prompted

You will be asked for:

File name

File format (csv or xlsx)

Database name

Host

Username

Password

Table name

5️⃣ Result 🎉

A table is created (if not already present)

Data is inserted into PostgreSQL successfully

🔮 Future Improvements

PostgreSQL → CSV export

Date & Boolean type detection

CLI arguments instead of input()

FastAPI integration

Chatbot interface

Docker support

⚠️ Limitations (for now)

All string values default to TEXT

No duplicate handling

No schema migration support

👨‍💻 Author

Fahad
Backend logic, database handling, and architecture designed and implemented independently.

⭐ Feedback & Contributions

Suggestions, issues, and improvements are welcome.
Feel free to fork and experiment.