#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ OOP PROPERTY, SETTER, DELETER DECORATOR KULLANIMI !!! //////////////////////////////////
#pythonda hazir halde bulununa decoratorleri inceliycez, classlara ozgu decoratorlere bakicaz..
#@property    @setter     @deleter

#ornek ile aciklayalim

# class Kisi:
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         #self.adsoyad = ad + " " + soyad                #ismi degistirdikten sonra guncellenmedigi icin bunu bastan email gibi bir fonksiyonda tanimlicaz.
#
#
#     @property
#     def adsoyad(self):
#         return f"{self.ad} {self.soyad}"            #bu simdi email gibi ayri bir fonksiyon oldugu icin direkt cagiramiyoruz bunu da () ile getiricez
#     @property
#     def email(self):
#         return f"{self.ad}.{self.soyad}@sirket.com"
#
#
# kisi1 = Kisi("Ali","Ulam")
#
# kisi1.ad = "Kaan"           #adsoyad daki isim eski isim kaldi cunku adsoyadin bellekte tutuldugu yer farkli ad ve soyadin tutuldugu yer farkli
#                             # email zaten ayri bir fonksiyon oldugu icin o hep en guncel ismi alacaktir. bu problemi nasl cozebiliriz peki adsoyad neden guncellenmedi
#                             # bunu da email gibi yapabiliriz. bir cozumdur.
#
# print(kisi1.ad)
# print(kisi1.soyad)
# #print(kisi1.adsoyad)           #adsoyad icin ayri bir fonksiyon olusturdugumuz icin artik boyle cagiramiyoruz, artik () ekleyerek cagirabiliyoruz. yani:
# #print(kisi1.adsoyad())          #email gibi parantezlerini ekleyerek cagiiryourz.
# print(kisi1.adsoyad)                #ARTIK PROTERTYU KULLANDIGIMIZ ICIN () KARAKTELERINI KULLANMAAY GEREK KALMIYOR
# #print(kisi1.email())            #burada butun ciktilarimiz normal sekilde cikiyor. peki ustteki gibi kisi1.ad i degistirirsek ne oluyor?
# print(kisi1.email)              #BRUADA DA ARTTIK PROTERTY KULLANDIGIMIZ ICIN () KULLANMADAN CAGIRABILIYORUZ.

#SIMDI GELELIM ONEMLI NOKTAYA, BIZ BURADA EMAIL VE ADSOYAD ARTIK BIR OZELLIK OLMADIGI ICIN () ILE CAGIRMAK ZORUNDA KALMISTIK AMMMMAAAAA
#BUNLARIN BASINA @PROTERTY EKLRSEK BU KEYWORD ARTIK BIZE BU FONKSIYONLARIN BIR OOP OZELLIGIYMIS GIBI DAVRANMASINI SAGLAYCAK VE DIREKT OLARAK KULLANMAMIZI MUMKUN KILACAK YANI
#BU EKSTRADAN YAZDIGIMIZ () LARI SILEBILICEZ ARTIK.

#property genel olarak bu ise yariyor. yani fonksiyonlari bir class in ozeligiymis gibi cagirabilmemizi sagliyor.





#\\\\\\\\\\\\\\\\\\\\\\\SIMDI GELELIM SETTER KULLANIMINA////////////////////////

#simdi normalde ozlelikleri biz direkt olarak ad = "Abdullah" diyerek atama yapabliyoruz hadi bakalim simdi @property ile duzenlediklerimizde yapabiliyor muyuz ona bakalim.

#kisi1.adsoyad = "Messi Leo"            # hayir yapamiyoruz object has no setter hatasini aliyoruz, tam olarak burada setter hazir decoratoru ihtiyacimizi karsiliyor

#simdi setter keywordunun nasil kullanildigini inceleycez.!!!


# class Kisi:
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         #self.adsoyad = ad + " " + soyad                #ismi degistirdikten sonra guncellenmedigi icin bunu bastan email gibi bir fonksiyonda tanimlicaz.
#
#
#     @property
#     def adsoyad(self):
#         return f"{self.ad} {self.soyad}"            #bu simdi email gibi ayri bir fonksiyon oldugu icin direkt cagiramiyoruz bunu da () ile getiricez
#     @property
#     def email(self):
#         return f"{self.ad}.{self.soyad}@sirket.com"
#
#     @adsoyad.setter         #yeni bir adsoyad set etme islemince bu calisacak.      #burada kullanacagimiz fonksiyon ismini vermemiz zorunludur.
#     def adsoyad(self,isim):     #simdi burada bosluga gore 1. kisim isim 2. kisim soysim olucak ona gore ayarlicaz.
#         ad,soyad = isim.split(" ")
#         self.ad = ad                    #buradaki ad ve soyadlari yukarida en yukarida class icinde tanimladigmiz ad ve soyadlara yolladk ve yeni ad soyadlar olusturduk....
#         self.soyad = soyad
#
#
#
#
# kisi1 = Kisi("Ali","Ulam")
#
# kisi1.ad = "Kaan"
#
# kisi1.adsoyad = "Messi Leo"             #bunu set etmeye calisirken ustteki @adsoyad.setter calisacak.
#
# print(kisi1.ad)
# print(kisi1.soyad)
# print(kisi1.adsoyad)
# print(kisi1.email)



#simdi del e gelelim simdi del diyip kisiyi ya da ozelligini silebiliyoruz ornek olarrak boyle:
# del kisi1
# del kisi1.ad
# del kisi1.soyad         #gibi gibi silme islemleri yapabiliyoruz.


#\\\\\\\\\\\\\\\\\\\\\\ DELE GECELIM ///////////////////////

# class Kisi:
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         #self.adsoyad = ad + " " + soyad                #ismi degistirdikten sonra guncellenmedigi icin bunu bastan email gibi bir fonksiyonda tanimlicaz.
#
#
#     @property
#     def adsoyad(self):
#         return f"{self.ad} {self.soyad}"            #bu simdi email gibi ayri bir fonksiyon oldugu icin direkt cagiramiyoruz bunu da () ile getiricez
#     @property
#     def email(self):
#         return f"{self.ad}.{self.soyad}@sirket.com"
#
#     @adsoyad.setter         #yeni bir adsoyad set etme islemince bu calisacak.      #burada kullanacagimiz fonksiyon ismini vermemiz zorunludur.
#     def adsoyad(self,isim):     #simdi burada bosluga gore 1. kisim isim 2. kisim soysim olucak ona gore ayarlicaz.
#         ad,soyad = isim.split(" ")
#         self.ad = ad                    #buradaki ad ve soyadlari yukarida en yukarida class icinde tanimladigmiz ad ve soyadlara yolladk ve yeni ad soyadlar olusturduk....
#         self.soyad = soyad
#
#     @adsoyad.deleter            #hepsinin isimleri ayni hepsi adsoyad, setter de deleter de property de biz hangi ture uygun islem yapacaksak otomatik olarak ona gidiyoruz.
#     def adsoyad(self):
#         print("silindi")
#         self.ad = None
#         self.soyad = None
#
#
#
# kisi1 = Kisi("Ali","Ulam")
#
# kisi1.ad = "Kaan"
#
# kisi1.adsoyad = "Messi Leo"             #bunu set etmeye calisirken ustteki @adsoyad.setter calisacak.
#
# del kisi1.adsoyad               #burada silindi yazisni ekrana yazdirdik, silmedik cunku silmesi icin gerekjli kodlari biz yazzmadik. ad soyada none dedirttik.
#
# print(kisi1.ad)
# print(kisi1.soyad)
# print(kisi1.adsoyad)
# print(kisi1.email)


#kisaca ozellik olarak erismek istedimgizde property calisiyor, atama yapmak istedigimizde setter decoraoru calsiyor, del ile bir seyi silmek istiyorsak deleter calisiyor.























