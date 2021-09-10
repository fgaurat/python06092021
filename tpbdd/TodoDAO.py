import sqlite3
from Todo import Todo

class TodoDAO:
    
    def __init__(self,*,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def find_all(self):
        cur = self._con.cursor()
        sql = r"SELECT id,title,completed FROM todos"
        result_set = cur.execute(sql)
        
        # result = [Todo(id=row[0],title=row[1],completed=row[2]) for row in result_set]
        result = []
        for row in result_set:
            t = Todo(id=row[0],title=row[1],completed=row[2])
            result.append(t)
        
        return result