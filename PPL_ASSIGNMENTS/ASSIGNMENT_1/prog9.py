import random
if __name__ == "__main__":
    v = random.randrange(1, 51)
    i = 1
    #c = 50
    flag = 0
    while i <= 4:
        n = input("Enter your choice between 1 and 50\n")
        n1 = int(n)
        '''if n1 > 50 or n1 < 1:
                 print("Your choice is beyond range\nEnter your choice less than or equal to 50 and greater than or equal to 1")'''
        if n1 == v:
            print("Congrats! Your choice is correct\n")
            flag = 1
            break
        elif v <= 10 and n1 > v:
            print("Your choice is wrong\nYour guess should be between 1 and 10 and less than this entered choice")
            #c /= 2
        elif v <= 10 and n1 < v:
            print("Your choice is wrong\nYour guess should be between 1 and 10 and greater than this entered choice")
        elif v <= 20 and n1 > v:
            print("Your choice is wrong\nYour guess should be between 11 to 20 and less than this entered choice")
            #c /= 2
        elif v <= 20 and n1 < v:
            print("Your choice is wrong\nYour guess should be between 11 to 20 and more than this entered choice")
        elif v <= 30 and n1 > v:
            print("Your choice is wrong\nYour guess should be between 21 and 30 and less than this entered choice")
            #c /= 2
        elif v <= 30 and n1 < v:
            print("Your choice is wrong\nYour guess should be between 21 and 30 and more than this entered choice")
        elif v <= 40 and n1 > v:
            print("Your choice is wrong\nYour guess should be between 41 and 50 and less than this entered choice")
            #c /= 2
        elif v <= 40 and n1 < v:
            print("Your choice is wrong\nYour guess should be between 41 and 50 and more than this entered choice")
        i += 1
    if flag == 0:
        print("Bad luck!\nBetter luck next time\n")


