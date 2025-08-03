from connection.connect import mysqlConnection

def update(table: str, columns: list[str], data: list[str]):
    
    b = ""
    for i in range(len(columns)):
        if i == len(columns) - 1:
            b += columns[i] + " = " + "'" + data[i] + "'"
        else:    
            b += columns[i] + " = " + "'" + data[i] + "'" + ", "

    stringQuery = f"UPDATE {table} SET {b}"
    conn = mysqlConnection().con()
    cursor = conn.cursor()
    
    try:
        cursor.execute(stringQuery)
        result = conn.commit()
        conn.close()
        return result   
    except Exception as e:
        return f"error: {e}"    