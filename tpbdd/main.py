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


def main_requests_json():
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


# CRUD
# Create => INSERT
# Retrieve Read => SELECT
# Update => UPDATE
# Delete => DELETE

def main():
    con = sqlite3.connect('bdd_todos.db')
    cur = con.cursor()
    sql = r"SELECT id,title,completed FROM todos"
    result_set = cur.execute(sql)
    
    for row in result_set:
        print(row)


    con.close()



if __name__ == '__main__':
    main()