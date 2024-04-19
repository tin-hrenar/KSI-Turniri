def swiss(l):
    length = len(l) // 3
    l1 = [() for i in range(length)]
    print(len(l))
    length = (len(l) - 1) // 3
    for i in range(len(l)):
        print(l1[i%length])
        print(tuple(l[i]))
        l1[i%length] += tuple(l[i])
    return l1



l = list(range(1, 13))
l = [str(i) for i in l]

print('a', swiss(l))
        
        
