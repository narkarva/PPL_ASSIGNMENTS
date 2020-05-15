#from __future__ import division
import math
def myfun(n):
    i, mysum, count = 1, 0.0, 0
    while i <= n:
        if n % i == 0:
            count += 1
            mysum += 1 / i
        i += 1
    a =  math.modf(count / mysum)
    if 0.0 in a:
        return 1
    else:
        return 0
if __name__ == "__main__":
    count, i = 0, 1
    while 1:
        a = myfun(i)
        if a == 1:
            print(i)
            count += 1
        if count == 10:
            break
        i += 1

            
