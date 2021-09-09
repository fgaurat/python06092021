import requests
import glob
import re

def main_requests():

    for i in range(1,5):
        file_name = f"apache_logs_{i:02}.log"
        url = f"http://logs.eolem.com/{file_name}"
        print(url)
        r = requests.get(url)
        with open(file_name,"w") as f:
            print(r.text,file=f)


# * => 0 ou n
# + => 1 ou n
# ? => 0 ou 1
# {3} => 3
# {3,5} => 3 min -> 5 max
# {3,} => 3 min -> n max



def main():
    log_files = glob.glob('*.log')
    print(log_files)
    for log_file in log_files[:1]: # limite au premier fichier
        with open(log_file) as f:
            lines = tuple(f.readlines())
            for line in lines:
                # r = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                r = "^(.+?)\s"
                result = re.search(r, line.strip())
                print(result.group(0))




if __name__ == '__main__':
    main()