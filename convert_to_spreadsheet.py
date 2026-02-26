import csv
import openpyxl
import os


class Convert_To_Spreadsheet:

    @staticmethod
    def create_file_by_name(name_of_file, extension, data, columns=None):

        if not data:
            print("No data to export.")
            return

        if columns is None or not columns:
            columns = list(data[0].keys())

        extension = extension.lower()

        if extension == "csv":
            Convert_To_Spreadsheet._export_csv(name_of_file, data, columns)

        elif extension == "xlsx":
            Convert_To_Spreadsheet._export_xlsx(name_of_file, data, columns)

        else:
            raise ValueError("Unsupported file format. Use 'csv' or 'xlsx'.")

    @staticmethod
    def _export_csv(filename, data, columns):
        filepath = f"{filename}.csv"

        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # write header
            writer.writerow(columns)

            # write rows
            for row in data:
                writer.writerow([row.get(col) for col in columns])

        print(f"CSV file created: {filepath}")

    @staticmethod
    def _export_xlsx(filename, data, columns):
        filepath = f"{filename}.xlsx"

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Data"

        # write header
        sheet.append(columns)

        # write rows
        for row in data:
            sheet.append([row.get(col) for col in columns])

        workbook.save(filepath)
        print(f"Excel file created: {filepath}")