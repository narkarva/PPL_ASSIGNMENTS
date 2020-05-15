import math
def myfun(n):
    i, mysum = 1, 0
    while i < n:
        if n % i == 0:
           mysum += i
        i += 1
    return mysum
if __name__ == "__main__":
    i, count = 2, 0
    '''
    c = myfun(220)
    print(c)
    c = myfun(284)
    print(c)
    '''
    while 1:
       c =  myfun(i)
       n = myfun(c)
       if i == c:
           i += 1
       elif i == n:
           print(n, c)
           count += 1
           i = c
       elif count == 10:
           break
       i += 1
