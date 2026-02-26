from import_spreadsheet_file import Import_Spreadsheet_File
from convert_to_database import Convert_To_Database
from import_database_data import Import_Database_Data
from convert_to_spreadsheet import Convert_To_Spreadsheet


# ---------- USER INPUT ----------
file_name = input("Enter file name (without extension): ").strip()
extension = input("Enter file extension (csv / xlsx): ").strip().lower()

database_name = input("Enter database name: ").strip()
host_db = input("Enter database host (default: localhost): ").strip() or "localhost"
user = input("Enter database user: ").strip()
password = input("Enter database password: ").strip()

table_name = input("Enter table name: ").strip()


choice = input(
    'Convert from:\n'
    '1. Spreadsheet to PostgreSQL\n'
    '2. PostgreSQL to Spreadsheet\n'
)

# ---------- OPTION 1 ----------
if choice == '1':
    spreadsheet = Import_Spreadsheet_File(file_name, extension)
    data = spreadsheet.load()

    if not data:
        raise ValueError("Spreadsheet is empty")

    db = Convert_To_Database(
        host=host_db,
        database=database_name,
        user=user,
        password=password
    )

    column_types = db.infer_column_types(data)

    sql_columns = [
        f'"{column}" {dtype}'
        for column, dtype in column_types.items()
    ]

    db.create_table(table_name, ", ".join(sql_columns))
    db.insert_data_in_rows(table_name, data)

    print("Spreadsheet successfully imported into PostgreSQL")

# ---------- OPTION 2 ----------
elif choice == '2':
    db = Import_Database_Data(
        host_db,
        database_name,
        user,
        password
    )

    if not db.check_if_table_exist(table_name):
        raise ValueError("Table does not exist")

    data = db.fetch_all_rows(table_name)
    columns = db.get_column_names()
    print(data)

    Convert_To_Spreadsheet.create_file_by_name(
        name_of_file=table_name,
        extension=extension,
        data=data,
        columns=columns
    )

    print("PostgreSQL table exported successfully")

else:
    print("Invalid choice")