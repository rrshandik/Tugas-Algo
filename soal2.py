# Ramadhan Surya Handika
#222410102070

sapi_Warrior = 690
sapi_Mage = 420
sapi_Assasin = 530
sapi_Nolep = 330
indeks_sapi = 0
umur_sapi = []
buat_umur = []
print ('''
Kode Sapi : 
1. sapi_Warrior = 690
2. sapi_Mage    = 420
3. sapi_Assasin = 530
4. sapi_Nolep   = 330 ''')
banyak_input = int (input("\nMau input berapa sapi?     : "))
print ("\n")
for x in range (banyak_input) :
    input_user = int(input (f"Masukkan kode sapi ke-{indeks_sapi+1}    : "))
    umur_sapi.append (input_user)
    if input_user == 1 :
        buat_umur.append (sapi_Warrior)
        indeks_sapi += 1
         
    elif input_user == 2 :
        buat_umur.append (sapi_Mage)
        indeks_sapi += 1
         
    elif input_user == 3 :
        buat_umur.append (sapi_Assasin)
        indeks_sapi += 1
         
    elif input_user == 4 :
        buat_umur.append (sapi_Nolep)
        indeks_sapi += 1
print ("\nInput :")
for x in umur_sapi :
    print (x)
print ("\nOutput :")
tahun = int(sum(buat_umur) / 365)
bulan = int((sum(buat_umur) - (tahun*365))/30)
hari = int(sum(buat_umur) - (tahun*365) - (bulan*30))

print (f"total umur dalam hari = {sum(buat_umur)} hari")
print (f"Jadi umurnya adalah {tahun} tahun, {bulan} bulan, {hari} hari\n")