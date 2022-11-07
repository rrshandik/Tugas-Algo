buat_harga = [] #ini nanti bakal diisi list harga ya
buat_diskon = [] #buat diisi list diskon
list_diskon = [] #daftar harga yang udah didiskon nanti masuk sini
i = 0 # buat jadi variabel indeks gaess

input_batas = int(input("Masukkan banyak barang: ")) #nentuin batas jumlah input user

for x in range (input_batas) :
    input_harga = int(input(f"Masukkan harga awal barang ke-{x+1}: "))
    buat_harga.append (input_harga) #ini nanti biar harganya masuk ke list kosong buat_harga
    
for y in range (input_batas) :
    input_diskon = int(input(f"Masukkan besar diskon (dalam persen) barange ke-{y+1}: "))
    buat_diskon.append (input_diskon) #ini nanti biar harganya masuk ke list kosong buat_diskon

for z in range (input_batas) :
    diskon = int(buat_harga [i]*(buat_diskon[i]/100)) # jadi nanti bakal mulai dari indeks ke-0 masing2 list
    list_diskon.append (diskon) #ini nanti biar harganya masuk ke list kosong list_diskon
    i += 1 # ditambah 1 biar ngulang trs sampe batas terpenuhi (batasnya di input_batas ya)

print (list_diskon)
print (f"Diskon terbesarnya di barang ke-{list_diskon.index(max(list_diskon))+1} : {max(list_diskon)}")
# xxx.index buat nyari posisi indeks, lalu ditambah 1 biar ga start dari 0 dan sesuai yg kita mau
# max buat nyari nilai max dalam sebuah list