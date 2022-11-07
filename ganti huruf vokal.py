teks = input ('ia apa : ')
pengganti = input ("huruf apa : ")

for x in 'aiueo' :
    teks = teks.replace(x, pengganti)
    
print (teks)