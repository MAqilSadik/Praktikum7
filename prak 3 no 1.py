try :
    file = open("d:/prak 3.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)

except ValueError :
    print(' input tidak valid')
