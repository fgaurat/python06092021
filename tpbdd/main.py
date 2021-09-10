from Todo import Todo
import requests
from pprint import pprint
import sqlite3
import configparser
import argparse

def insert_todo(todo,con):

    cur = con.cursor()


    sql = f"""
        INSERT INTO todos(title,completed) 
        VALUES ('{todo['title']}',{todo['completed']})
    """
    cur.execute(sql)
    con.commit()


def main_requests_json():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print()

    con = sqlite3.connect(config['BDD']['name'])

    url = config['DATA']['url']
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

# Data Access Object => DAO
# Repository
# 
# ORM : Object Relation Mapping
# Class => table
# props => colonnes
# 1 objet => 1 ligne

def main_select():
    parser = argparse.ArgumentParser(description='Insert todos from web in sqlite')
    parser.add_argument('config',help='configuration file',type=str,default='config.ini')
    args = parser.parse_args()
    config = configparser.ConfigParser()
    config.read(args.config)
    con = sqlite3.connect(config['BDD']['name'])
    cur = con.cursor()
    sql = r"SELECT id,title,completed FROM todos"
    result_set = cur.execute(sql)
    
    for row in result_set:
        t = Todo(id=row[0],title=row[1],completed=row[2])
        print(t)

    con.close()

def main():
    



if __name__ == '__main__':
    main()