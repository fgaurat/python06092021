import requests

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    resp = requests.get(url)
    todos = resp.json() 
    print(todos)


if __name__ == '__main__':
    main()