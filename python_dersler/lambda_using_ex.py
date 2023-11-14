# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Lambda Fonksiyonları //////////////////////////////////

#normalde olusturdugumuz fonksiyonlar su sekilde oluyor:

# def kare_al(x):
#     return x * x
# print(kare_al(5))

#bu siradan normal bir fonksiyon olusturma tarzimizdir simdi bunu lambda ile olusturmayi ogrenelim:


#lambda ile:

#lambda yazmamiz bir fonksiyon tanimlayacagimiz anlamina geliyor.

# kare_al = lambda x : x * x
# #burada : dan onceki kisim fonksiyonun aldigi parametre oluyor. : dan sonraki kisim ise geri donduurlecek degeri iceeriyor.
# print(kare_al(6))               #gordugunuz gibi ayni fonksiyon gibi kullanabiliyoruz.

# kup_al = lambda x : x ** 3
# print(kup_al(7))


#simdi iki parametreliler icin orneklendirelim.

# toplam = lambda x, y : x + y            #normal fonksiyonlari tanimlarkenkiyle benzer seyler
# print(toplam(5,9))

#simdi ise belirli olmayan sayida parametre ile bu islemi yapalim..

# genel_toplam = lambda *args: sum(args)              #burada gordugumuz gibi fonksiyonlardaki *args ayni gecerlidir.
# print(genel_toplam(2,65,2,5,7,2,5,8,8,3,2,345,3456,5))



#Simdi ise bunlari bir degiskene atamadan direkt olarak fonksiyon olusturucaz ve ekrana yazdiricaz. usttekiler gibi bunlari bir degiskene atamak zorunda degiliz.

# print(lambda x,y,z : x * y + z)                 #bunu bu sekilde yazdirirsaniz fonksiyon olduugnun ciksitisni alacaksiniz.

#print((lambda x,y,z : x * y + z)(3,4,5))                #kullanimini bu sekilde vererek parmetreleri girip sonucumuzu alabiliyoruz.

#print(int((lambda *args : sum (args) / len(args))(2,3,4,5,6,7,8)))          #lambda fonksiyonlarini isim vermeden anonim olarak da kullaniyoruz.

#buna neden ihtiyac var?
#Birincisi fonksiyonlari lambda ile ifade etmek daha kisa
#ikinci olarak programimizda fonksiyonu bir kere kullanacaksak ayri bir fonksiyon ismi kullanmamiza gerek yok, bunu bir lambda ile olusturmak daha mantikli.
#ama birden fazla kullanicaksak tabi normal kullanmamiz mantikli
#ve ilerde gorecegiz bazi fonksiyonlar parametre olarak fonksiyon aliyorlar onlar icin de bu lambda kullanimi iyi oluyor.

#simdi guzel bir uygulama yapalim:

# liste = [("Ali", 20), ("Kaan", 24), ("Tuana", 22), ("Emel", 24)]
# # liste.sort()
# #print(liste)                #simdi burada sirlama kararini 1. parametreye gore aldi peki biz diger parametreye gore siralama yapmasini istersek ne yapabiliriz.:
#
# liste.sort(key= lambda x: x[1])  #sort un bir keywordu var o da key. key keywordxu bizden bir fonksiyon istiyor. burada x ("Ali",20) oluyor cunku elaman bu.
#                             #buradan da demek elemanlarinin icindeki 1. elemanlara gore dondurmesini soyluyoruz,
# print(liste)                #burada artik yaslara gore siralandilar.

#simdi bruada ayri bir fonksiyon siralamamiza gerek yok burada lambdayla direkt olarak kolaylikla yaptik
#bunu fonksiyonla yapsaydik soyle yapacaktik.:

# def yas_sirala(x):
#     return x[1]
# liste.sort(key = yas_sirala)           #Fonksiyonla yapsaydik boyle fopnksiyon tanimlayip sonrasinda sort icine fonksiyonu atamamiz gerekecekti.




#Baska bir ornege gecelim simdi de liste degil de sozlukler olsun


# liste2 = [{"Ad": "Osman", "Soyad": "Yutkun", "Yas": 22},{"Ad": "Lokman", "Soyad": "Imtur", "Yas": 35},{"Ad": "Rukiye", "Soyad": "Kilic", "Yas": 19}]
# liste2.sort(key= lambda x : x["Soyad"])         #soyad anahtarina gore siraliycaz.
# print(liste2)

#avantaji ise bir cok fonksiyon parametre ile fonksiyon aldigi icin kullanimi cok kolay oluyor. lambda ile kolayca hallediyoruz





























