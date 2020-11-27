file = open("d:/dataMHS.txt", "r")
input('masukkan nama file : ')

print(file.read())

while True:
    file = open("d:/dataMHS.txt", "a")
    data = input('data yang mau ditambahkan:')
    file.write(data + 'n')
    file.close()
    print('mau lagi (y/n):')
    jawab = input()
    if jawab == 'n':
        break
