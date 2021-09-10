import requests
from pprint import pprint

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    resp = requests.get(url)
    todos = resp.json() 
    # print(todos)
    # pprint(todos)
    # print(todos[0])

    for todo in todos:
        print(todo['title'],todo['completed'])


if __name__ == '__main__':
    main()