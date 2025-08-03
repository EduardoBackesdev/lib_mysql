from connection.connect import mysqlConnection

def insert(table: str, columns: list[str], data: list["str"]):
    
    c = ""
    d = ""
    for i in range(len(columns)):
        if i == len(columns) - 1:
            c += columns[i]
        else:        
            c += columns[i] + ', '
            
            
    for i in range(len(data)):
        if i == len(data) - 1:
            d +=  "'" + data[i] + "'"
        else:        
            d += "'" + columns[i] + "'" + ', '      
                            
    stringQuery = f"INSERT INTO {table} ({c}) VALUES ({d});"
    
    conn = mysqlConnection().con()
    
    query = conn.cursor()
    
    try:
        query.execute(stringQuery)
        result = conn.commit()
        conn.close()
        return result      
    except Exception as e:
        return f"Error executing query: {e}"
    
    