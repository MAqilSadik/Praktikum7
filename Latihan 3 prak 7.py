r = True
sum = 0
jumlah = 0

while(r == True):
    
    try :
            
        bil = int(input('Masukkan Bilangan Bulat : '))
        sum += bil
        jumlah += 1
        
        pilihan = input('Tambah Lagi ? (y/n) : ')

        if(pilihan == 'y') :
            r = True
            
        elif(pilihan == 'n') :
            r = False

    except ValueError:
            print('Bukan Bilangan Bulat')
            continue
    
ratarata = sum / jumlah

print('Rata-Ratanya Adalah:', ratarata)
