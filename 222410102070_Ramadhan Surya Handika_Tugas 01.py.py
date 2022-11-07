print (4* '=', "Program Angka Ganjil Genap", 4* '=')

angka = int(input("\nMasukkan Angka : "))
if (angka % 2 == 0 and angka <10 ) :
    print (angka, "adalah bilangan genap dan merupakan bilangan kecil")
elif (angka % 2 == 0 and angka >= 10 and angka <50) :
    print (angka, "adalah bilangan genap dan merupakan bilangan sedang")
elif (angka % 2 == 0 and angka >= 50) :
    print (angka, "adalah bilangan genap dan merupakan bilangan besar")
elif (angka % 2 != 0 and angka <10 ) :
    print (angka, "adalah bilangan ganjil dan merupakan bilangan kecil")
elif (angka % 2 != 0 and angka >= 10 and angka <50) :
    print (angka, "adalah bilangan ganjil dan merupakan bilangan sedang")
elif (angka % 2 != 0 and angka >= 50) :
    print (angka, "adalah bilangan ganjil dan merupakan bilangan besar")
    
print (" \n Semoga Membantu!")