from connection.connect import mysqlConnection

def update(table: str, columns: list[str], data: list[str]):
    
    conn = mysqlConnection().con()
    cursor = conn.cursor()