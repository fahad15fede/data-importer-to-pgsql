import psycopg2
from psycopg2.extras import RealDictCursor

class Import_Database_Data():
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host = host,
            database = database,
            user = user,
            password = password
            )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)  #Connection established

    def check_if_table_exist(self, table_name):
        query = f'''SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public' AND 
        table_name = %s
        );
        '''
        self.cursor.execute(query,(table_name,))
        result = self.cursor.fetchone()
        return result['exists']

    
    def fetch_all_rows(self, tablename):
        query = f'SELECT * FROM {tablename}'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
    
    def get_column_names(self):
        return[desc.name for desc in self.cursor.description]

    def close_connection(self):
        self.cursor.close()
        self.conn.close()    
    
        