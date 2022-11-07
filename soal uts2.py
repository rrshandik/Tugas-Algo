x = int(input())
y = int(input())
z = int(input())

if x in range(1,51) and y in range(1,51) and z in range(1,51):
    if x<y:
        print(0)
    else:
        print(z//(x-y))