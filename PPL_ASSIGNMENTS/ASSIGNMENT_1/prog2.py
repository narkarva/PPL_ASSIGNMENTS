if __name__ == "__main__":
    s1 = {"TIGER", "GOAT", "GRASS_BUNDLE"}
    l1 = ["MAN"]
    l2 = []
    while len(l2) != 3: #"TIGER" not in l2 or "GOAT" not in l2 or "GRASS_BUNDLE" not in l2:
        a = s1.pop()
        if a == "GRASS_BUNDLE" and "TIGER" in s1 and "GOAT" in s1:
            s1.add(a)
        elif a == "TIGER" and "GOAT" in s1 and "GRASS_BUNDLE" in s1:
            s1.add(a)
        elif (a == "TIGER" and "GOAT" in l2) or (a == "GOAT" and "GRASS_BUNDLE" in l2):
            if len(l2) != 2:
                l1.append(a)
                print("Forward", l1)
                b = l2.pop()
                l2.append(a)
                l1.pop()
                #s1.add(b)
                l1.append(b)
                print("Backward", l1)
                b = l1.pop()
                s1.add(b)
            elif len(l2) == 2:
                l1.append(a)
                print("Forward", l1)
                l2.append(a)
                l1.pop()
                break
        else:
            l1.append(a)
            print("Forward", l1)
            l2.append(a)
            l1.pop()
    
