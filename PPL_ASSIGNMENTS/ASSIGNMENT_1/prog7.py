def missing_page_numbers(l1, n):
    i = 1
    l2 = []
    while i <= n:
        if i not in l1:
            l2.append(i)
        else: 
            pass
        i += 1
    return l2
if __name__ == "__main__":
    #l1 = []
    l1 = [2,4,5,6,12,16,17,20,21]
    #while int(input()) != -1: 
        #l1.append()
    l2 = missing_page_numbers(l1, 25)
    print("Page numbers present in the book are")
    print(l1)
    print("Missing page numbers in the book are")
    print(l2)
    #for i in l2:
        #print(i)


