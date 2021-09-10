import requests
from pprint import pprint
import sqlite3

def insert_todo(todo,con):

    cur = con.cursor()


    sql = f"""
        INSERT INTO todos(title,completed) 
        VALUES ('{todo['title']}',{todo['completed']})
    """
    cur.execute(sql)
    con.commit()


def main():
    con = sqlite3.connect('bdd_todos.db')

    url = "https://jsonplaceholder.typicode.com/todos"
    resp = requests.get(url)
    todos = resp.json() 
    # print(todos)
    # pprint(todos)
    # print(todos[0])

    for todo in todos:
        insert_todo(todo,con)
        print(todo['title'],todo['completed'])

    con.close()

if __name__ == '__main__':
    main()