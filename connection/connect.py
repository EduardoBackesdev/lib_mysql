import mysql.connector

class mysqlConnection:
    
    c = None
    
    def con(self):   
        
        host = ""
        user = ""
        password = ""
        database = ""
         
        try:
            self.c = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            return self.c
        except mysql.connector.Error as err:
            return err
        
    def close(self):
        self.c.close()
            
        
            