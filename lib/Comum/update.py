from connection.connect import mysqlConnection

def update(table: str, columns: list[str], data: list[str]):
    
    a = {}
    for i in range(len(columns)):
        a[columns[i]] = data[i]
        
    print(a)
    exit()    
        
    
    stringQuery = f"UPDATE {table} SET"
    conn = mysqlConnection().con()
    cursor = conn.cursor()