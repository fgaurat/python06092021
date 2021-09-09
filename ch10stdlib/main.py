import requests
import glob

def main_requests():

    for i in range(1,5):
        file_name = f"apache_logs_{i:02}.log"
        url = f"http://logs.eolem.com/{file_name}"
        print(url)
        r = requests.get(url)
        with open(file_name,"w") as f:
            print(r.text,file=f)

def main():
    log_files = glob.glob('*.log')
    print(log_files)

if __name__ == '__main__':
    main()