from connection.connect import mysqlConnection

def delete(table: str):
    
    stringQuery = f"DELETE FROM {table}"
    
    print(stringQuery)
    exit()
    
    conn = mysqlConnection().con()
    query = conn.cursor()
    
    try:
        query.execute(stringQuery)
        result = conn.commit()
        conn.close()
        return result
    except Exception as e:
        return f"Error executing query: {e}"
   
    