# """print("Oyuncu Kaydetme Programı:")
# ad = input("Oyuncunun Adı:")
# soyad = input("Oyuncunun Soyadı:")
# takim = input("Oyuncunun Takimi:")
#
# bilgiler = [ad,soyad,takim]
#
# print("Bilgiger Database'e Kaydediliyor......")
#
# print("Oyuncunun Adı: {} \nOyuncunun Soyadı: {} \nOyuncunun Takımı: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
# print("Kaydedildi..")"""
#
#
# ''''defkullanici = "yazilimcibebe"
# defparola = "1234"
#
# kullanici = input("Kullanici adi:")
# parola = input("Parola:")
#
# if((defkullanici == kullanici) and (defparola == parola)):
#     print("Sisteme Hosgeldiniz")
# elif((defkullanici != kullanici) and (defparola == parola)):
#     print("Kukllanici adi Yanlis!")
# elif((defkullanici == kullanici) and (defparola != parola)):
#     print("Sifre yanlis")
# else:
#     print("Tekrar dene!") '''
#
#
# '''sonuc = 1
#
# for i in range(0,10):
#     sonuc *= 2
#
# print(sonuc)'''
#
#
# """"liste1 = ["a" , "b", "c"]
# liste2 = [1,2,3]
#
# for harf in liste1:
#     for sayi in liste2:
#         print(harf,sayi)"""


# x = 2
# y = 3
#
# while x * y < 1000:
#     print(x,y)
#     x += 2
#     y+= 2
# print (x,y)

# i = 1
# while True:
#     print(i)
#     i += 1
#     if i == 1000:
#         break


# i = 1
# while True:
#     if i %2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1
#     if i == 1000:
#         break



# dict={
#     'Isim': 'Mesut',
#     'yas': 24,
#     'lokasyon':{
#         'yasadigi sehir': 'Koln',
#         'Dogdugu sehir': 'Istanbul'
#
#     }
# }
# print(dict.items())


# i=0
# while (i<10):
#     i+=1
#     print(i)


# sayi = int(input("Sayi gir:"))
# sonuc = 1
#
# i = 1
# while i <= sayi:
#     sonuc *= i
#     i+=1
# print(f"{sayi}! = {sonuc}")




# sayi = int(input("Sayi gir: "))
#
# asal = True
#
# for i in range(2, sayi):
#     if sayi % i == 0:
#         asal = False
#         break
# if asal == True:
#     print(f"{sayi} Asal")
# else:
#     print(f"{sayi} Asal Degil")



# sayi = int(input("Lutfen sayi giriniz:"))
#
#
# count = 0
#
# for bolen in range(1, sayi+1):
#     if sayi % bolen != 0:
#         print(f"Bolunmeyen sayilar {bolen}")
#         continue
#     elif sayi % bolen == 0:
#         count += 1
#         print(f"Bolunen sayilar {bolen}")
#
# print(f"{sayi} sayisinin Toplam {count} adet boleni var" )




# sayi = int(input("Sayi gir: "))
#
# str_sayi = str(sayi)
#
# toplam = 0
#
# for i in str_sayi:
#     toplam += int(i)
# print(f"Rakamlar Toplami: {toplam}")


# sayi = int(input("Sayi gir: "))
#
# toplam = 0
#
# gecici = sayi
#
# while gecici != 0:
#     basamak = gecici % 10
#     toplam += basamak
#     gecici //= 10
# print(toplam)



# liste = []
#
# for i in range(5):
#     sayi = int(input("Sayi gir: "))
#     liste.append(sayi)
#     liste.sort()
#     print(liste)
# print(f"Listenizin son hali {liste}")



# sayi = int(input("Sayi gir: "))
#
# for i in range(1,sayi):
#     if i * i == sayi:
#         print(f"{sayi} sayisi {i}'nin karesidir.")
#     else:
#         continue


# sayi = int(input("Sayi gir: "))
#
# kare = sayi ** 0.5
#
# while kare > 0:
#     if kare == int(kare):
#         print(f"{sayi} sayisi tamkaredir")
#         break
#     else:
#         print(f"{sayi} sayisi tamkare degildir.")
#         break



# metin = input("Metin gir")
#
# sozluk = dict()
#
# for harf in metin:
#     if harf in sozluk:
#         sozluk[harf] += 1
#     else:
#         sozluk[harf] = 1
# for harf , adet in sozluk.items():
#     print(harf , adet)




# metin = input("Metin gir: ")
# metin2 = ""
#
# for i in metin:
#     if i == "a":
#         metin2 += "A"
#     else:
#         metin2 += i
# print(f"Yeni metniniz = {metin2}")



# asal_list = list()
#
# asal_list.append(2)
#
# sayi = 3
#
# while True:
#     asal = True
#     for i in range(2, int(sayi ** 0.5) + 1):
#         if sayi % i == 0:
#             asal = False
#             break
#     if asal:
#         asal_list.append(sayi)
#         if len(asal_list) == 10000:
#             break
#     sayi += 1
#
# liste2 = []
# for asal in asal_list:
#     strasal = str(asal)
#     if strasal.startswith("3") and strasal.endswith("7"):
#         liste2.append(asal)
# print(liste2)
# print(len(liste2))




# liste = []
#
# for i in range(100, 1000):
#     toplam = 0
#     gecici = i
#     while gecici != 0:
#         basamak = gecici % 10
#         toplam += basamak ** 3
#         gecici //= 10
#     if toplam == i:
#         liste.append(i)
# print(liste)



# fibonacci_list = []
#
# fibonacci_list.append(1)
# fibonacci_list.append(1)
# gecici = 0
# while True :
#     if len(fibonacci_list) != 100:
#         gecici = fibonacci_list[-1] + fibonacci_list[-2]
#         fibonacci_list.append(gecici)
#     if len(fibonacci_list) == 100:
#         break
# print(fibonacci_list)



# fibonacci_list = []
#
# fibonacci_list.append(1)
# fibonacci_list.append(1)
#
# for i in range (2,100):
#     fibonacci_list.append(fibonacci_list [i-1] + fibonacci_list [i - 2])
#
# print(fibonacci_list)




# fibonacci_list = []
#
# fibonacci_list.append(1)
# fibonacci_list.append(1)
# sayi = ""
# gecici = 0
#
# while True :
#     sayi = str(gecici)
#     if len(sayi) != 1000:
#         gecici = fibonacci_list[-1] + fibonacci_list[-2]
#         fibonacci_list.append(gecici)
#     if len(sayi) == 1000:
#         print(sayi)
#         break



# def ortalama_hesapla(liste):
#     toplam = sum(liste)
#     adet = len(liste)
#     ortalama = toplam / adet
#     print("Sayilarin ortalamasi", ortalama)
#
# ortalama_hesapla([1,2,3,4,5,6,7])




# def buyuk_harf(metin):
#     metin = metin.upper()
#     print(metin)
# buyuk_harf("pskljdfklsfdg")


# def selamla(mesaj,isim = "Anonim"):
#     print(f"{mesaj} {isim}.")
#
# selamla("Merhaba")



# def indirim(fiyat, yuzde = 15) :
#     indirim_miktari = fiyat * (yuzde / 100)
#     indirimli_fiyat = fiyat - indirim_miktari
#     print(f"indirimli fiyat: {indirimli_fiyat}")
#
# indirim(100, 4)




# def ortalama(x,y):
#     return (x + y) / 2
#
# a = ortalama(2,6)
# b = ortalama(7,3)
# print(f"a ortalamasi {a} b ortalamasi {b}")



# def buyuk(metin):
#     return metin.upper()
#
#
# a = buyuk("selamss")
#
# print(a)




# from math import *
# # import math
#
# sonuc = factorial(5)
# sonuc2 = sqrt(634546)
# print(sonuc , sonuc2)



# import mat_modul
#
# sonuc = mat_modul.cember(4)
#
# print(sonuc)


# import mat_modul as mat
#
# sonuc = mat.cember(45)
# print(sonuc)




# import os
# import time
# import datetime
# import selenium



# import random

# for i in range (10):
#     print(random.randrange(1,10))



# import random
#
# liste = ["siyah", "beyaz", "mor", "gri", "beyaz"]
#
# print(random.sample(liste,5))


# import random
#
# zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# for i in range(1000000):
#     zar = random.randint(1,6)
#     zarlar[zar] += 1
#
# for zar in zarlar:
#     print(f"{zar} gelme olasiligi: {zarlar[zar] / 1000000}")



# import random
#
# alti_alti = 0
# deneme_sayisi = 0
# while True:
#     deneme_sayisi += 1
#     zar1 = random.randint(1,6)
#     zar2 = random.randint(1,6)
#     if zar1 + zar2 == 12:
#         alti_alti += 1
#     if alti_alti == 10:
#         print(f"10 kere 6-6 gelmesi icin zarlar {deneme_sayisi} kadar atildi")
#         break





# import time
#
# baslangic = time.time()
# liste = []
# for i in range(10000000):
#     liste.append(i)
# bitis = time.time()
# print(bitis - baslangic)



# import time
# zaman = time.strftime("%d:%m:%Y %I:%M:%S %p")
# print(zaman)
# print(type(zaman))


# import time
# print("Program baslatildi")
# time.sleep(3)
# print("Program sonlandi")





# from datetime import date

# bugun = date.today()
# # print(bugun)
# # print(type(bugun))
# # print(bugun.year)
# # print(bugun.day)
# # print(bugun.month)
# # print(bugun.weekday())
# # print(bugun.isoweekday())
#
#
#
# # bu date ile fonksiyonlar olusturabiliyoruz mesela bu taihten simdiki tarihe kadarki vakte gecen sureyi ya da girdigimiz gunun ne oldugunu soyler
# gecmis_tarih = date(2015,8,13)
# # print(gecmis_tarih.weekday())
#
# gecen_zaman = bugun - gecmis_tarih
# print(gecen_zaman)
# print(type(gecen_zaman))



# from datetime import date
# from datetime import datetime
# bugun = date.today()
#
# suan = datetime.now()
#
# # print(suan)
# # print(suan.ctime())
# # print(suan.month)
#
# gecmis_an = datetime(2014,5,26,6,46,32,123)
# print(suan-gecmis_an)



# from datetime import date
# from datetime import datetime
# bugun = date.today()
#
# suan = datetime.now()
#
# print(datetime.strftime(bugun,"%d:%m:%Y"))
# print(suan.strftime("%d:%m:%Y"))




# from datetime import date
# from datetime import datetime
# from datetime import timedelta

# suan = datetime.now()
# print(suan.month)
# print(suan.date())
# print(suan.day)
# print(suan.year)
# print(suan.second)
# print(suan.time())

# suan = datetime.now()
# tdelta = timedelta(days=7,hours=5,seconds=69)
# print(suan + tdelta)
# print(suan - tdelta)



# from datetime import datetime
#
# pazar_sayisi = 0
#
# for yil in range(1901, 2001):
#     for ay in range (1,13):
#         if datetime(yil,ay,1).weekday() == 6:
#             pazar_sayisi +=1
# print(pazar_sayisi)




# import os
# from datetime import datetime

#mkdir, makedirs klasor olusturma komutlari. rmdir, removedirs(ici bos dosyalari siler), remove klasor silme
#os.rename("deneme1", "Deneme1234")   rename ile ayni zamanda dosyalarin yerini de degistirebiliyoruz. askldjjklasd/asdjkhhjaks/sdjkfhhjksdf/sakdjfjksdf/Deneme121111323 mesela

# print(os.stat("venv").st_mtime)
# zaman = datetime.fromtimestamp(os.stat("venv").st_atime)
# print(zaman)



# import os

# for gecerli_klasor, icindeki_klasorler, icindeki_dosyalar in os.walk("C:\\Users\\pcan_\\Desktop\\pyhoncalisma"):
#     print("Gecerli Klasor:", gecerli_klasor)
#     print("Icindeki Klasorler", icindeki_klasorler)
#     print("Icindeki Dosyalar", icindeki_dosyalar)
#     print()




# import os
#
# print(os.path.splitext("C:\\Users\\pcan_\\Desktop\\pyhoncalisma\\main.py"))

# print(os.path.join("Deneme1","\\Deneme2","Deneme3"))

# print(os.path.isdir("C/Users/pcan_/Desktop/pyhoncalisma/Deneme1234"))


# GIRILEN ADRESTEKI DOSYALARI UZANTILARINA GORE KLASORLERE AYIRIP DUZENLEME
# import os
#
# def duzenle():
#     klasor = input("Duzenlenecek Klasor: ")
#     dosyalar = []  #dosyalar depolanacak
#     uzantilar = [] #uzantilar depolanacak
#     def list_dir():
#         for dosya in os.listdir(klasor):
#             if os.path.isdir(os.path.join(klasor,dosya)): #dosyami bir klasor mu
#                 continue
#             if dosya.startswith("."): #dosyamiz gizli dosya mi
#                 continue
#             else:
#                 dosyalar.append(dosya)
#     list_dir()
#     #uzantilari alma
#     for dosya in dosyalar:
#         uzanti = dosya.split(".")[-1]
#         if uzanti in uzantilar: #uzanti onceden eklendi mi
#             continue
#         else:
#             uzantilar.append(uzanti)
#
#     for uzanti in uzantilar: #klasorler olusturuluyor
#         if os.path.isdir(os.path.join(klasor,uzanti)):
#             continue
#         else:
#             os.mkdir(os.path.join(klasor,uzanti))
#     for dosya in dosyalar:
#         uzanti = dosya.split(".")[-1]
#         os.rename(os.path.join(klasor,dosya),os.path.join(klasor,uzanti,dosya))
#
# if __name__ == "__main__":
#     duzenle()




# TARIHE GORE SIRALAMA
# import os
# from datetime import datetime
#
# def duzenle():
#     klasor = input("Duzenlenecek Klasor: ")
#     dosyalar = []  #dosyalar depolanacak
#     tarihler = [] #tarihler depolanacak
#     def list_dir():
#         for dosya in os.listdir(klasor):
#             if os.path.isdir(os.path.join(klasor,dosya)): #dosyami bir klasor mu
#                 continue
#             if dosya.startswith("."): #dosyamiz gizli dosya mi
#                 continue
#             else:
#                 dosyalar.append(dosya)
#     list_dir()
#     #tarihleri alma
#     for dosya in dosyalar:
#         tarih_damgasi = os.path.getctime(os.path.join(klasor, dosya))
#         tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
#         if tarih in tarihler:
#             continue
#         else:
#             tarihler.append(tarih)
#
#
#     for tarih in tarihler: #klasorler olusturuluyor
#         if os.path.isdir(os.path.join(klasor,tarih)):
#             continue
#         else:
#             os.mkdir(os.path.join(klasor,tarih))
#     for dosya in dosyalar:
#         tarih_damgasi = os.path.getctime(os.path.join(klasor, dosya))
#         tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
#
#         os.rename(os.path.join(klasor,dosya),os.path.join(klasor,tarih,dosya))
#
# if __name__ == "__main__":
#     duzenle()





# with open("deneme.txt") as f:
#     for satir in f:
#         print(satir,end="")
#   satir = f.readline()
#   print(satir,end="")
#   pozisyon = f.tell()
#   print(pozisyon)
#   f.seek(0)
#   satir = f.readline()
#   print(satir, end="")



# with open("deneme.txt") as f:
#     okunacak_miktar = 10
#     icerik = f.read(okunacak_miktar)
#     while len(icerik) > 0:
#         print(icerik,end="")
#         icerik = f.read(okunacak_miktar)  #kaldigi yerden devam ediyor. sonraki 10 a geciyor



# with open("deneme.txt") as okunacak:
#     with open("deneme2.txt", "w") as yazilacak:
#         icerik = okunacak.readlines()
#         for satir in icerik:
#             yazilacak.write(satir)



# with open("C:\\Users\\pcan_\\Desktop\\pyhoncalisma\\ertas.jpg","rb") as okunacak:
#     with open("ertas2.png","wb") as yazilacak:
#         okunacak_miktar = 1024
#         icerik = okunacak.read(okunacak_miktar)
#         while len(icerik) > 0:
#             yazilacak.write(icerik)
#             icerik = okunacak.read(okunacak_miktar)


# with open("C:\\Users\\pcan_\\Desktop\\pyhoncalisma\\ertas.jpg","rb") as okunacak:
#     with open("ertas3.png","wb") as yazilacak:
#         for satir in okunacak:
#             yazilacak.write(satir)



# METHODLARI LISTE HALINDE YAZDIRMA

# list_methods = []
# for method in dir(list):
#     if method.startswith("__"):
#         continue
#     list_methods.append(method)
#
# set_methods = []
# for method in dir(set):
#     if method.startswith("__"):
#         continue
#     set_methods.append(method)
#
# string_methods = []
# for method in dir(str):
#     if method.startswith("__"):
#         continue
#     string_methods.append(method)
#
# tuple_methods = []
# for method in dir(tuple):
#     if method.startswith("__"):
#         continue
#     tuple_methods.append(method)
#
# dict_methods = []
# for method in dir(dict):
#     if method.startswith("__"):
#         continue
#     dict_methods.append(method)
#
# basliklar = ["List Methods", "Set Methods", "String Methods","Tuple Methods","Dict Methods"]
# classes = [list_methods, set_methods, string_methods, tuple_methods, dict_methods]
#
# max_len = 0
# for class_ in classes:
#     if len(class_) > max_len:
#         max_len = len(class_)
#
# with open("Methods.txt", "w") as f:
#     for baslik in basliklar:
#         print(baslik, end="")
#         print(" " * (30-len(baslik)),end="")
#         f.write(baslik)
#         f.write(" " * (30 - len(baslik)))
#     for i in range(max_len):
#         print()
#         f.write("\n")
#         for class_ in classes:
#             if i >= len(class_):
#                 print("_______", end="")
#                 print(" " * 23, end="")
#                 f.write("_______")
#                 f.write(" " * 23)
#             else:
#                 print(class_[i],end="")
#                 print(" " * (30 - len(class_[i])),end="")
#                 f.write(class_[i])
#                 f.write(" " * (30 - len(class_[i])))




# with open("ornek_metin.txt", encoding="utf-8") as f:
#     with open("gecenler.txt", "w")as g:
#         with open("kalanlar.txt", "w") as k:
#             icerik = f.readlines()
#             m = 0
#             for satir in icerik:
#                 if m == 0:
#                     m +=1
#                     continue
#                 satir = satir.replace("\n", "") # replace metodu bir yaziyi digeriyle degistirmeye yariyor
#                 bosluk_sayisi = 0
#                 bosluk_indexleri = []
#                 index = 0
#                 for karakter in satir:
#                     if karakter == " ":
#                         bosluk_sayisi += 1
#                         bosluk_indexleri.append(index)
#                     index += 1
#                 ad_soyad = satir[:bosluk_indexleri[0]]
#                 soyad = ad_soyad.split("-")[-1]
#                 ad = ad_soyad[:ad_soyad.index(soyad) -1].replace("-", " ")
#                 notlar = satir.split(" ")[-1]
#                 notlar = notlar.split("/")
#                 birinci_vize = int(notlar[0])
#                 ikinci_vize = int(notlar[1])
#                 final = int(notlar[2])
#                 ortalama = birinci_vize * 0.3 + ikinci_vize * 0.3 + final * 0.4
#                 bolum = satir[bosluk_indexleri[0]+1:bosluk_indexleri[-1]]
#                 if ortalama >= 70 and final >= 70:
#                     g.write(ad)
#                     g.write(" " * (25 - len(ad)))
#                     g.write(soyad)
#                     g.write(" " * (25 - len(soyad)))
#                     g.write(bolum)
#                     g.write(" " * (25 - len(bolum)))
#                     g.write(str(round(ortalama,1)))
#                     g.write(" " * 21)
#                     g.write("Gecti")
#                     g.write("\n")
#
#                 else:
#                     k.write(ad)
#                     k.write(" " * (25 - len(ad)))
#                     k.write(soyad)
#                     k.write(" " * (25 - len(soyad)))
#                     k.write(bolum)
#                     k.write(" " * (25 - len(bolum)))
#                     k.write(str(round(ortalama, 1)))
#                     k.write(" " * 21)
#                     k.write("Kaldi")
#                     k.write("\n")




# numbers = [1,2,3,4,5,6,7,8,9]
#
# list2= []
# for number in numbers:
#     list2.append(number)
# print(list2)
#
# list3= [number for number in numbers]
# print(list3)


# numbers = [1,2,3,4,5,6,7,8,9]
# list3 = [number * number for number in numbers]
# print(list3)


# numbers = [1,2,3,4,5,6,7,8,9]
# list3 = [number for number in numbers if number %2 == 0]  #kosul varsa en sona yazilir
# print(list3)



# numbers = [1,2,3,4,5,6,7,8,9]
# list3 = [number * number for number in numbers if number %2 == 0]
# print(list3)


# numbers = [1,2,3,4,5,6,7,8,9]
# list3 = [number * number for number in numbers if number %2 == 0 and number > 4]
# print(list3)






# numbers =  [1,2,3,4]
# letters = "abcd"
#
# list3 = [(number,letter) for number in numbers for letter in letters]
# print(list3)




# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [2,3,6,9,5]
#
# list3 = [number * number for number in list1 if number not  in list2]
# print(list3)



# list_ = [[1,2,3], [4,5,6], [8,9,10,11,12]]
#
# list3= [j for i in list_ for j in i]
# print(list3)



# list_methods = []
# list3 = [method for method in dir(list) if not method.startswith("__")]
# print(list3)



# try:
#     a = 5
#     b = 2
#     # if b == 0:
#     #     raise ZeroDivisionError
#     c = a/b
#     x = 5
#     d = x
#     isim = "Ali"
#     karakter = isim[2]
#     list_ = [1,2,3]
#     m = list_[5]
#
# except ZeroDivisionError as e:
#     print(e)
# 
# except NameError as e:
#     print(e)
#
# except IndexError as e:
#     print(e)
#
# except Exception as e:
#     print(e)
#
# else:
#     print("else blogu calisiyor")
#     print(c)
#     print(karakter)
# finally:
#     print("finally blogu calisiyor")


































