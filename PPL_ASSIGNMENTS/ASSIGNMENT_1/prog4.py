import numpy
if __name__ == "__main__":
    a = numpy.ndarray((3,3))
    b = numpy.ndarray((3,1))
    l = numpy.ndarray((3,3))
    u = numpy.ndarray((3,3))
    x = numpy.ndarray((3,1))
    i, j = 0, 0
    print("Enter elements of coefficient matrix\n")
    while i < 3:
        j = 0
        while j < 3:
            n = input()
            n1 = int(n)
            a[i][j] = n1
            j += 1
        i += 1
    j = 0
    print("Enter elements of b  matrix\n")
    while j < 3:
        n = input()
        n1 = int(n)
        b[j][0] = n1
        j += 1
    i,j = 0,0
    while i < 3:
        l[i][i] = 1
        i += 1
        j += 1
    i, j = 0, 1
    while j < 3:
        l[i][j] = 0
        j += 1
    l[1][2] = 0
    i = 0
    u[1][0] = 0
    u[2][0] = 0
    u[2][1] = 0
    for j in range(0, 3):
        u[i][j] = a[i][j]
    j = 0
    #u[1][0], u[2][0], u[2][1] = 0, 0, 0
    for i in range(1,3):
        l[i][0] = a[i][j] / u[0][0]
    i = 1
    for j in range(1,3):
        u[i][j] = a[i][j] - (l[i][0] * u[i - 1][j])
    if u[1][1] == 0:
        print("System is inconsistent\n")
    else:
        l[2][1] = (a[2][1] - l[2][0] * u[0][1]) / u[1][1]
    #u[1][0], u[2][0], u[2][1] = 0, 0, 0
        i = 1
    #for j in range(1,3):
       # u[i][j] = a[i][j] - (l[i][0] * u[i - 1][j])
        u[2][2] = a[2][2] - l[2][0] * u[0][2] - l[2][1] * u[1][2]
        print("Lower triangular matrix is\n", l, "\nUpper triangular matrix is\n", u)
        if numpy.linalg.det(u) == 0.0 or numpy.linalg.det(l) == 0.0:
            print("System is inconsistent\n")
        else:       
            x1 = numpy.ndarray((3, 3))
            u1 = numpy.linalg.inv(u)
            l1 = numpy.linalg.inv(l)
            x1 = numpy.dot(u1, l1)
            x = numpy.dot(x1, b)
            print("Solution of given system of equatons is\n",x)



