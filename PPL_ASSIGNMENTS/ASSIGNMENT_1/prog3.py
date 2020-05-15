import math
def armstrong(n):
    mysum = 0.0
    while n != 0:
        r = n % 10
        mysum += math.pow(r, 3)
        n //= 10
    return mysum
if __name__ == "__main__":
    n = input("Enter any positive number\n")
    #print(type(n))
    n1 = int(n)
    #print(type(n1))
    i = 1
    while i <= n1:
        c = armstrong(i)
        if c == i:
            print(i)
        i += 1

