total_harga = 0
input_user = "y"

while input_user == "y":
    masuk1 = float(input ("Masukkan Harga Barang : "))
    masuk2 = float(input ("Masukkan Harga Satuan : "))
    total1 = masuk1*masuk2
    total_harga = total1+total_harga
    input_user = input ("Apakah Masih Ada lagi? [y]/[g] : ")
    if input_user != "y" :
        if input_user != "g" :
            input_user = input ("Apakah Masih Ada lagi? [y]/[g] : ")
print ("Total Harga adalah Rp", (total_harga))

