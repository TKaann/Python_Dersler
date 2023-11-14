# \\\\\\\\\\\\\\ Reduce Fonksiyonu Kullanimi ////////////////////
#map ve filter ile benzerlikleri de vardir farkliliklari da.
#map ve filter fonksiyonlariyla benzerligi sudur: parametre olarak fonksiyon ve liste aliyor
#farki ise: diger 2 fonksiyon bize liste donduruypr ama reduce fonksiyonu bize sadece tek bir deger donduuryor hemen orneklendirmeye gecelim:

# from functools import reduce
#ayrica functools modulunun icinden import etmemiz gerekli.
#
# liste = [2,4,6,9]
#
# def toplama(x,y):
#     return x + y
#
# def carpma(x,y):
#     return x * y
#
# sonuc1 = reduce(toplama,liste)
# print(sonuc1)
#
# #simdi burada buldugu sonucu soyle buldu: ilk once 2 ve 4 u topladi 6 buldu sonra 6 ile 6 yi topladi 12 oldu sonra 12 ile 9 u toplayip 21 sonucunu buldu ve esitledi.
#
# sonuc2 = reduce(carpma, liste)
# print(sonuc2)       #burada da yukardaki ayni islem yapiliyor.



#simdi lambda ile yapalim

# liste = [2,4,6,9]
# sonuc1 = reduce(lambda x, y : x + y, liste)
# print(sonuc1)
#
# sonuc2 = reduce(lambda x, y : x * y, liste)
# print(sonuc2)
# #ayni sonuclari lambda ile aldik.






#simdi daha anlamli ornekler yapalim
#simdi bunlarin ekok unu alalim, ebob var ama ekok pythonda yok ebobu impoert edelim.
# from math import gcd
#
# liste = [2,4,6,9,10]   #ebob(a,b) * ekok(a,b) = a*b        ekok(a,b) = a * b / ebob(a,b)     ekok 2 sayinin carpimlarinin ebobuna bolumuyle olusuyor yani, biz de onu yaptik.
#
# def ekok(x,y):
#     return int((x * y) / gcd(x,y))
# # print(ekok(6,8))
#
# ekok_ = reduce(ekok,liste)
# print(ekok_)






#simdi tas kagit makas oyunu yapalim

# def tkm(x,y):
#     kume = {x,y}
#
#     if x == y:
#         return x
#
#     if kume == {"tas","makas"}:
#         return "tas"
#
#     if kume == {"tas","kagit"}:
#         return "kagit"
#
#     if kume == {"kagit","makas"}:
#         return "makas"
#
# liste = ["makas","kagit","tas","makas","kagit","makas","makas"]
# sonuc = reduce(tkm,liste)
# print(sonuc)

























































