from import_spreadsheet_file import Import_Spreadsheet_File
from convert_to_database import Convert_To_Database


# ---------- USER INPUT ----------
file_name = 'Coffee_smit'
extension = 'csv'
database_name = 'swiggy_res_data'
host_db = 'localhost'
user = 'postgres'
password = 'fahad15fede'
table_name = 'coffee_table'


# ---------- LOAD FILE ----------
spreadsheet = Import_Spreadsheet_File(file_name, extension)
data = spreadsheet.load()

if not data:
    raise ValueError("Spreadsheet is empty")


# ---------- CONNECT DATABASE ----------
db = Convert_To_Database(
    host=host_db,
    database=database_name,
    user=user,
    password=password
)

#-----------CREATE TABLE----------------


# ---------- INFER COLUMN TYPES ----------
column_types = db.infer_column_types(data)

sql_columns = []
for column_name, column_type in column_types.items():
    sql_columns.append(f'"{column_name}" {column_type}')

final_sql_columns = ", ".join(sql_columns)


# ---------- CREATE TABLE ----------
db.create_table(table_name, final_sql_columns)
db.insert_data_in_rows(table_name, data)