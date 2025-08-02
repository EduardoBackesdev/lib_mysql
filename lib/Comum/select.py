from connection.connect import mysqlConnection

def select(table: str, columns: list[str]):
    
    c = ""
    for i in range(len(columns)):
        if i == len(columns) - 1:
            c += columns[i]
        else:        
            c += columns[i] + ', '
    stringQuery = f"SELECT {c} FROM {table};"
    
    conn = mysqlConnection().con()
    
    query = conn.cursor()
    
    try:
        query.execute(stringQuery)
        result = query.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"Error executing query: {e}"
    
    
    
    
    
        
    
    