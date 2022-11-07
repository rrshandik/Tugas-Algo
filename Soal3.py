# Ramadhan Surya Handika
# 222410102070

kiri = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v']
kanan = ['y','u','i','o','p','h','j','k','l','m','n','b']
input_user = input ("Masukkan Kata : ")
huruf = True

for x in range(len (input_user)-1) :
    if input_user [x] in kiri :
        if input_user [x+1] in kiri : 
            print ("\nFalse")
            print (f"Penjelasan : Ada karakter yang berdempetan, yakni '{input_user[x]}' dan '{input_user [x+1]}' di jari kiri")
            huruf = False
    if input_user [x] in kanan :
        if input_user [x+1] in kanan :
            print ("\nFalse")
            print (f"Penjelasan : Ada karakter yang berdempetan, yakni '{input_user[x]}' dan '{input_user [x+1]}' di jari kanan")
            huruf = False
if huruf == True :
    print ("\nTrue")
    print ("Penjelasan : Setiap karakter selalu bergantian tangan")