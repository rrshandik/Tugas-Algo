input_user = int(input())
angka = []

for i in range(input_user):
    x = int(input())
    angka.append(x)
    
for x in angka:
    total = 0
    for y in range(1, x):
        if x % y == 0:
            total += y
    print(total)