import pymysql.cursors

class MySQLConnection:
    def __init__(self, db) -> None:
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True
        )
        self.connection = connection

    def query_db(self, query, data):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f"Running Query: {query}")
                cursor.execute(query, data)
                if query.lower().find('select'):
                    results = cursor.fetchall()
                    return results
                elif query.lower().find('insert'):
                    self.connection.commit()
                    return cursor.lastrowid
                else:
                    self.connection.commit()
            except Exception as e:
                print(f'Something Went Wrong: {e}')
            finally:
                self.connection.close()

def connectToMySQL(db : str) -> MySQLConnection:
    return MySQLConnection(db)
