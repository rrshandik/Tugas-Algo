# membuat program game tebak-tebakan
# Ramadhan Surya Handika
# 222410102070

import random
import os

angka = int(random.randint (0, 100))
percobaan = 1

print ("\nSelamat Datang di Game Guess Your Luck!")
input_user = input ("Apakah Anda ingin bermain? [Y/T]: ")
if input_user == "Y" or input_user == "y" :
    main = True
    print ("\nRULES :")
    print ("1. Anda diberikan kesempatan untuk menebak angka sebanyak tujuh (7) kali percobaan.")
    print ("2. Anda akan dinyatakan kalah apabila sudah menebak melewati batas.")
    print ("3. Semoga Beruntung!\n")
   
    while main == True and percobaan < 8 :
        
        while percobaan <= 7 :
            game = int(input("Masukkan tebakanmu : "))
            if game < angka :
                print ("Tidak tepat, angka terlalu kecil")
            elif game > angka :
                print ("Tidak tepat, angka terlalu besar")
            elif game == angka :
                print (f"Tebakan Anda tepat. Anda menebak sebanyak {percobaan} kali")
                exit ()
            percobaan += 1
        
            if percobaan == 8 :
                main = False
                print ("\nAnda sudah menebak sebanyak 7 kali. Maaf, Anda kurang beruntung")
                break
                exit ()
            
            
elif input_user == "T" or input_user == "t" :
    print ("Diterima, terima kasih!")