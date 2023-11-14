#\\\\\\\\\\\\\\\\\\\\\\!!!!!!!!!!!!!!!!!!!!!!!!  *args, **kwargs KULLANIMI !!!!!!!!!!!!!!!!!!!!!!////////////////////////////

#\\\POSITIONAL ARGUMENT..

# def kuvvet_al(x,y): #Bunlar positional arguments olarak geciyor. hepsi tam girilmeli eksik veya fazla degil
#
#     return x ** y

# print(kuvvet_al(3,3))  # yani fonksiyonu cagirdigimizda icine girdigimiz ilk deger fonksiyon icindeki ilk degiskene 2. deger ise sirasiyla diger degiskene ataniyor.

# print(kuvvet_al(5))  #boyle calistirdigimizda hata verecektir 1 tane parametre eksik diye geri donus yapacaktir. positional parametre ekik diyecektir.!!

# print(kuvvet_al(5,6,7))  #bunu yaparsak yine hata verecektir. positional fonkiyon 2 parametre istiyor sen 3 tane giriyorsun diye.


#\\\\KEYWORD ARGUMENT...

# def bilgi_ver(ad,soyad,yas = "Girilmedi"):   #bu tip onceden parametre verdigimiz fonksiyonlar ise Keyword Argument diye geciyor.
#     return f"Isim: {ad} Soyad: {soyad} Yas: {yas}"

# print(bilgi_ver("Hamit","Altintop"))   #bize ciktiyi verecektir varsayilan yas degerini kullanacaktir. eksik veya fazla parametre girersek hata verecektir.


#\\\KEYWORD PARAMETRE..

# def bilgi_ver2(ad = "Girilmedi",soyad = "Girilmedi",yas = "Girilmedi"):   #Ad ve yasi girmek istersek
#     return f"Isim: {ad} Soyad: {soyad} Yas: {yas}"

# print(bilgi_ver2("Hamit",yas = 34))  #bu Keyword Parametre de ise soyad girmeden sira bagimsiz fonksiyon icindeki ozelligimize atama yapabiliyoruz.



# def bilgi_ver3(ad = "Girilmedi",soyad = "Girilmedi",yas = "Girilmedi"):
#     return f"Isim: {ad} Soyad: {soyad} Yas: {yas}"
#
# #print(bilgi_ver3())   #hicbirsey girmeden sadece default degerleri bastirdik
#
# print(bilgi_ver3(soyad="Kobino", yas=28))   #isim harici keyword atamalariyla sira bagimsiz soyad ve yas girdik.





#\\\\\\\\\\\\ARGS KWARGS KAVRAMLARI////////////

#Esas konuya geliyoruz simdiz biz asagidaki gibi toplamalar yapmak istiyorsak ve toplamak istedigimiz sayilar git gide artarsa asagidaaki gibi bir yol izlemek yerine

# def topla2(x,y):
#     return x + y
#
#
# def topla3(x,y,z):
#     return x + y + z
#
# def topla4(x,y,z,t):
#     return x + y + z + t


#BU sekilde tek tek bunlari girmek yorucu olacaktir. ya da kac tane sayi toplayacagimiz kesin net degilse bu sekilde bir kullanim yapamayiz bunun yerine soyle yapyoruz.
# * operatorunden faydalaniyoruz bunun icin.


# def topla (*args):
#     print(args)               #burda args ile fonksiyon icine atilan butun elemanlari cekebiliyoruz, bizim elle tek tek girmemize gerek kalmiyor.
#
#
# topla(1,2,3,4,5,"Husam")

# def topla (*args):              #!!!!! bunlar demetle tutuluyor.
#     for arg in args:
#         print(arg)                  #alt alta yazdirdik burda da mesela.
# topla(1,2,3,4,5,"Husam",True)


# def tip (*args):
#     print(type(args))               #burada da type inin tuple oldugunu yani demet oldugunu goruyoruz.
# tip()


# def carp (*args):
#     carpim = 1
#     for sayi in args:
#         carpim *= sayi
#     #print(carpim)              #bu sekilde fonksiyonun icinden printi cagirabilirsiniz
#     return carpim
# #carp(2,3)                  #fonksiyon icinden cagirildigi icin tekrardan print yazmaya gerek yok
# print(carp(2,3))                #disarda da print icine tanimlayip yazdirabiliriz.


# def ortalama(*args):
#     return sum(args) / len(args)          #kac tane args girildiyse o kadar sum ve lenlerini alip boluyor ortalama aliyor, tek tek girmemize gerek kalmiyr.
# print(ortalama(5,20,15))



# def selamla(mesaj, *args):          #1 adet pozisyonel veri ekledik, o da mesaj nesnesi oluyor. yani ilk girilen deger mesaj nesnesi olacaktir. ondan sonrakiler args
#     sonuc = ""
#     sonuc += mesaj
#     sonuc += " "
#     for arg in args:            #argslar burada donguye alinip hepsi sonuc degiskenine ekleniyor ama ilk once mesaj nesnemiz geliyor.
#         sonuc += arg
#         sonuc += " "                #her args eklendikten sonra aralrina bosluk da ekliyoruz.
#     return sonuc                        #sonuc degiskenini return ediyoruz sonuc degiskenimiz butun totaldeki yazilanlari tutuyor.
#
# print((selamla("Merhabalar", "Ali", "Nasilsin")))



#!!!!!!\\\\\\\\\\\\\kwargs keyword arguments anlamina geliyor kwargs ise kw argumanlarini tutuyor. onun da paramteresi 2 yildiz yani ** seklinde.////////////

# def fonksiyon (**kwargs):           #girdigimiz keyword argumentlari Sozluk Dict olarak saklar....
#     print(kwargs)
#
#
# fonksiyon(ad= "ali", soyad="kolomoko", yas="26")                #kwargs sozluk olarak saklar, istedigimiz kadar atama yani nesne girebilirz.



# def fonk2 (zorunlu, *args, **kwargs):
#     print(zorunlu)                      #yazilmasi zorunlu olan nesnenin degeri yazdiriliyor.
#     print("Zorunlu alan yani pozisyonel alan yazdirildi.")
#     for arg in args:
#         print(arg)      #obur parametreler yazdiriliyor..
#     print("args degerleri yazdirildi.")
#     for kwarg in kwargs:
#         print(kwarg)    #BRUADA SADECE KEYLERI YAZDIRIYOR, VALUE DEGERLERINI DEGIL. YANI SOZLUKLEDE YAZDIR DEDIGIMIZDE SADECE KEY DEGERLERI YAZDIRILIR.
#
# #fonk2(2,3,4,5,"argsdayim hala", adi="kwargsa gectim", yas=23)      #kwargsta sadece keyler yazdirildi.
#
#
# #KWARGSTA HEM KEY HEM VALUE YAZDIRMAK ICIN 1 DEGISKEN DAHA ATAYIP ONA DA ITEMS LERI ATAMAMIZ GEREKIYOR YANI GOSTERECEK OLURSAK:
#
#     for k,v in kwargs.items():
#         print(k,v)    #BRUADA SADECE KEYLERI YAZDIRIYOR, VALUE DEGERLERINI DEGIL. YANI SOZLUKLEDE YAZDIR DEDIGIMIZDE SADECE KEY DEGERLERI YAZDIRILIR.
#
# fonk2(2,3,4,5,"argsdayim hala", adi="kwargsa gectim", yas=23)      #kwargsta sadece keyler yazdirildi.


#burada gordugunz gibi kwargs in degerleri de yazdirildi.

#\\\\\\\\\\\NOT: 1!!!!!!!!!     * DAN SONRA ARGS YAZMAMIZ ZORUNLU DEGIL *DAN SONRA ISTEDIGIMIZ YAZABILIRIZ YANI * ARGS YERINE *MERHAMA YAZABILIYORUZ CALISACAKTIR!!!!!//////////







