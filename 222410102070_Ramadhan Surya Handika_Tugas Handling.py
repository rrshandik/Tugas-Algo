
x = open ('./lupa weh/pertama.txt', 'a')
konten_baru = "\nMata kuliah favoritnya adalah 'Algo'"
print ("After : ")
x.insert(2, konten_baru)
x.close

with open ("./lupa weh/pertama.txt", 'r') as x : 
    print (x.read())
