from connection.connect import mysqlConnection

def selectWhere(table: str, columns: list[str], params):
    
    c = ""
    for i in range(len(columns)):
        if i == len(columns) - 1:
            c += columns[i]
        else:        
            c += columns[i] + ', '
    stringQuery =f"SELECT {c} FROM {table} "
    
    conn = mysqlConnection().con()
    
    cursor = conn.cursor()
    
    try:
        cursor.execute(stringQuery)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"Error executing query: {e}"
    
    
    
    
    
        
    
    