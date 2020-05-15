#import math
if __name__ == "__main__":
    n = input("Enter first term of geometric series\n")
    a = float(n)
    n1 = input("Enter common ratio of geometric series\n")
    r = float(n1)
    print("First 10 terms of geometric series are")
    for i in range(0, 10):
        print(a * r ** i )

