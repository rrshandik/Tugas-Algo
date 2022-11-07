input_user = input().lower()
kodenya = ''

enkrpsi = []

for i in input_user:
    enkrpsi.append(ord(i))

for  i in enkrpsi:
    if chr(i).isalpha():
        kodenyaPertambahan = i + 13
        selisih = 0
        if kodenyaPertambahan > 122:
            selisih = 13 - (122 - i)
            kodenya += chr(96 + selisih)
        else:
            kodenya += chr(kodenyaPertambahan)
    else:
        kodenya += chr(i)

print(kodenya)