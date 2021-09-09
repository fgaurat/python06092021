import requests

def main():
    url = "http://logs.eolem.com/apache_logs_01.log" 
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':
    main()