# belajar list

#indeks +   0   1   2   3
nomor =    [7, 20, 27, 100]
#indeks -  ... -3  -2  -1

print (nomor[1]); """kalo diluar list maka bakalan error"""
print (nomor[-3])
print (type(nomor))

"""append itu buat nambahin tapi di belakang list"""
print (nomor)
nomor.append(666)
print(nomor)

"""insert buat naro di sesuai yang mana"""
nomor.insert(2, 555)
print(nomor)