import random
if __name__ == "__main__":
    print("Enter N to exit dice simulation otherwise Enter Y")
    while  input() != 'N':
        b = random.randrange(1, 7)
        print(b)
        print("Do you want to continue?")



