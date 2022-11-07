kata_input = []
indeks_huruf = 0
input_jumlah = int(input ("\nIngin menginput berapa kata? : "))

for x in range(input_jumlah) :
    input_user = input ("Masukkan Kata : ")
    kata_input.append (input_user)

print ("\nInput :")
for x in kata_input :
    print (x)

for x in kata_input :
    print ("\nHasil :")
    for y in x :
        if indeks_huruf < len (x)-1 :
            if ord (x[indeks_huruf]) < ord (x[indeks_huruf+1]) :
                selisih = ord (x[indeks_huruf+1]) - ord (x[indeks_huruf])
                print ((x[indeks_huruf], "lebih kecil dari", (x[indeks_huruf+1]), "dan selisihnya adalah", selisih))
                indeks_huruf += 1
            elif ord (x[indeks_huruf]) > ord (x[indeks_huruf+1]) :
                selisih = ord (x[indeks_huruf]) - ord (x[indeks_huruf+1])
                print ((x[indeks_huruf], "lebih besar dari", (x[indeks_huruf+1]), "dan selisihnya adalah", selisih))
                indeks_huruf += 1
            elif ord (x[indeks_huruf]) == ord (x[indeks_huruf+1]) :
                selisih = ord (x[indeks_huruf]) - ord (x[indeks_huruf+1])
                print ((x[indeks_huruf], "sama besar dengan", (x[indeks_huruf+1]), "dan selisihnya adalah", selisih))
                indeks_huruf += 1
        elif indeks_huruf == len (x)-1 :
            indeks_huruf = 0
            print ("\n")
        