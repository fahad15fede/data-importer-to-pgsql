import csv, openpyxl, os

class Import_Spreadsheet_File:
    def __init__(self, file_name, extension):
        self.file_name = file_name
        self.extension = extension.lower()
        self.file_path = f"{file_name}.{extension}"
        self.data = []

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path} not found")

        if self.extension not in ["csv", "xlsx"]:
            raise ValueError("Only CSV and Excel files are supported")

    def load_csv(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

    def load_excel(self):
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active

        rows = list(sheet.iter_rows(values_only=True))
        headers = rows[0]

        for row in rows[1:]:
            self.data.append(dict(zip(headers, row)))

    def load(self):
        self.validate_file()

        if self.extension == "csv":
            self.load_csv()
        elif self.extension == "xlsx":
            self.load_excel()

        return self.data