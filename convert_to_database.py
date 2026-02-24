import psycopg2
from psycopg2.extras import RealDictCursor


    
class Convert_To_Database:

    
    def __init__(self, host = 'localhost', database = 'database_name', user = 'postgres', password = 'admin123' ):
        self.conn = psycopg2.connect(
            host = host,
            database = database,
            user = user,
            password = password
            )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
    
    def create_table(self, table_name, final_sql_columns):

        self.cursor.execute(
            f''' create table if not exists {table_name}(
                {final_sql_columns}
                );'''
        )
        self.conn.commit()
    
    def insert_data_in_rows(self, table_name, data):
        columns = list(data[0].keys())
        column_names = ', '.join(f'"{col}"' for col in columns)
        placeholders = ', '.join(['%s']*len(columns))

        query = f'''
                INSERT INTO {table_name} ({column_names})
                VALUES ({placeholders})
            '''
        

        for row in data:
            values = tuple(row[col] for col in columns)
            self.cursor.execute(query, values)
        
        self.conn.commit()

    def infer_column_types(self, data):

        column_types = {}

        columns = list(data[0].keys())

        for column in columns:
            values = []
            for row in data:
                value = row[column]

                if value is not None and value != '':
                    values.append(value)

            if not values:
                column_types[column] = "TEXT"
                continue

            is_integer = True
            for v in values:
                try:
                    int(v)
                except ValueError:
                    is_integer = False
                    break

            is_float = True
            for v in values:
                try:
                    float(v)
                except ValueError:
                    is_float = False
                    break

            if is_integer:
                column_types[column] = "INTEGER"
            elif is_float:
                column_types[column] = "NUMERIC(8,3)"
            else:
                column_types[column] = "TEXT"
        return column_types




        