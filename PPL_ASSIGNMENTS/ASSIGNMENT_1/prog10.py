import requests
if __name__ == "__main__":
    a = input("Enter url to be checked\n")
    a = requests.get(a)
    print(a.status_code)
    if a.status_code == 451:
        print("Website is blocked\n")
    else:
        print("Website is fine\n")
