from operator import truediv
from tkinter import Y



    
cek = True
while cek :
    print ("masukkan lagi deck")
    p = True
    while p :
        x = input("kamu maunya apa y or g : ")
        if x == "g" :
            p = False
            cek = False
        elif x != "y" :
            p = False
            cek = True
    print ("terima kasih")
    
bintang = int(input("Mau berapa star : "))
for i in range(bintang) :
    print ("*"*(i+1))