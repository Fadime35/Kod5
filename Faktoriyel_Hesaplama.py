#Faktöriyel Hesaplama
"""
0!=1     4!=24
1!=1     5!=120
2!=2     6!=720
3!=6
"""

sayi=int(input("Bir sayı giriniz:"))
carpim=1
i=1
while(1<=i<=sayi):
    carpim*=i
    i+=1
print(carpim)





