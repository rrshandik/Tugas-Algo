""" len itu buat mengetahui panjang list/kayanya jumlahnya ada berapa  """

list1 = [1,"hai",3,"namaku",4,"siapa"]
print (list1)
print (list1 [0:2]); """ini artinya dari
data (indeks) ke-0 sampai data ke-2"""
print (list1 [0::2]); """ini buat ngeprint datanya longkap 2"""
print (list1 [2:6:2]); """ini nanti dari indeks 2<= x < 6"""

list1 = [1, 2, 3]
list1.pop(); """ini kalo dalam kurungnya g
diisi maka yang dihapus otomatis hyang data terakhir"""
print (list1)

list2 = [1, 3, 5, 7]
del list2[2]
print (list2)

list3 = [2,4,6,8]
list3.remove (6); """ini yang dihapus itu data dalam list or indeksnya ya"""
print (list3)

#NOT IN DAN IN
list = ["yoga", "adalah", "manusia"]
print ("ganteng" in list)
print ("aku" not in list)

#dictionary
fruits = {
    'fruit1' : "pisang",
    'fruit2' : "mangga"
}

print(fruits['fruit2'])
print (fruits['fruit1'])

dict = {
    "halo" : "dunia",
    "hello" : "world",
    "ohayo" : "babayo",
}

print(f"dictionary sebelum diubah {dict}")
del dict["halo"]
print(f"dictionary setelah diubah {dict}")
dict.pop ("ohayo")

