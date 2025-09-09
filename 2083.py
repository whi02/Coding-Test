for j in range(3) :
    userInput = input().split()
    count = 0
    for i in userInput :
        if i == '1':
           count += 1


    if count == 1 :
        print('A')
    elif count == 2 :
        print('B')
    elif count == 3 :
        print('C')
    elif count == 0 :
        print('D')
    elif count == 4 :
        print('E')
