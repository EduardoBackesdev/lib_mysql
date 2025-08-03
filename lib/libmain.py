from lib.Comum.select import select
from lib.Comum.insert import insert
from lib.Comum.delete import delete

class libmain:
    
    # ----------  Common ---------- #
    # Select method 
    def select(self, table: str, columns: list[str]):
        return select(table, columns)
    
    # Insert method
    def insert(self, table: str, columns: list[str], data: list[str]):
        return insert(table, columns, data)
    
    # Delete method
    def delete(self, table:str):
        return delete(table)
    