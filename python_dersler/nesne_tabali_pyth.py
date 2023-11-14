#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ NESNE TABANLI PYTHON CALSIMA /////////////////////////////////////

#   SINIF VE ORNEK KAVRAMLARI (CLASS AND INSTANCE)
#   CLASS OLUSTURMA
#   OZELLIK VE METOTLAR (ATTRIBUTES AND METHODS)

#   CLASS (ORTAK OZELLIKLERI OLAN NESNELERI GRUPLAMAK)

# class calisan:                      #CLASS OLUSTURDUK ICINE HICBIR SEY YAZMADIK PASS LA GECTIK.
#     pass                             #CALISAN CLASSINI OLUSTURURKEN MIRAS ALIYOR OLSAYDIK ICI DOLU OLSAYDI () KULLANMAMIZ GEREKIYORDU.
#
# calisan1 = calisan()                 #CLASIMIZLA BGLANTILI NESNEMIZI OLUSTUUYOEUZ
#
# calisan1.name = "Alí"               #NESNEYE OZELLIKLER EKLIYORUZ
# calisan1.surname = "Veli"
# calisan1.age = 20
#
# print(calisan1.name, '\n' + calisan1.surname)       #BURADA TEK PRINT ICINDE ALT ALTA YAZIYORUZ /N ILE FAKAT NORMAL YAZARSAK BOSLUK BIRAKIYOR ALTTAKINI BASINA O YUZDEN 2. DEGISKEN ONCESI + KOYDUK

#BU SUANDA CLASS YAPISINA AYKIRI DURUMDA. ORTAK OZELLIKLI BIR NESNELER YOK SUAN GOSTERMEDLIK CLASS NASIL OLUSTURULUR DIYET NORMALDE BOYLE KUKLLKANIMAZ.




#\\\\\\\\\\\\\\\\\\\\\BURADA DEGISKENLER VBE NESNELERIN OZELLIKLERINI AYNI DEGIL FARKLI YAPIYORUZ KI ANLASILSIN////////////////////////


# class calisan:
#     def __init__(self,a,b,c):
#         print("__init__ fonksiyonu calisiyor")
                                                              #BURADA SELF BIZIM OLUSTURUGUMUZ NESNE YERINE GECIYOR VE GIRDIGIMIZ DEGERLERI FONKSIYON ICINDEKILERE ESITLIYOR.


#         self.name = a
#         self.surname = b                           #DEGISKEN OLAN CALISAN1 CALISAN CLASSI ICINDEKI INIT FONKSIYONUNDAKI DEGERLERE ESITLIYORUZ.
#         self.age = c
# calisan1 = calisan("Ali", "Veli", 20)                  #BURADA GIRDIGMIZ DEGERLER INIT SAYESINDE FONKSIYON ICINE GIRIYOR VE CALISAN CLASINDAKI DEGERLERE ATANIYOR.
                                                    #ORAYA ATANAN DEGERLERI SONRADAN OLUSTURDUGUMUZ NESNELERE ATIYORUZ.

# print(calisan1.name, calisan1.surname, calisan1.age)

#A B VE C ILE DEGISTIRDIK DAHA ANLASILABILIR OLMASI ICIN...




#/////////////////NORMAL KULLANIM ORNEKLENDIRMELERI////////////////////////\\\\\\\\\\\\\

# class calisan:
#     def __init__(self,name,surname,age):                     #DEF FONKSIYON TANIMLAAM ZATEN. __INIT__ ISE INITIALIZE DAN GELIYOR OLABILIR INIT BIR FONKSIYONDUR YANI BASLAT OLUSTUR.
#         #print("__init__ fonksiyonu calisiyor")                    # INIT ILK DEGERLERI BASLANGIC KONUMUNU TUTAR INIT ONEMLIDIR.
#                                                              #ILK INIT FONKSIYONU CALISIYOR
#                                                          #INITIN SELF DIYE BIR PARAMETRESI DE VAR. BUNLAR NESNELERIN OZELLIKLERINI TUTAR ONA YARIOYOR. DAHA DINAMIK YAPIYOR. VE OKUNURLUGU ARTIRIYOR.
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#                                 # BIR CLASS A BAGLI FONKYIYONLARA METOT DENIR... BURADA BIR METOT OLUSTURUYORUZ
#     def show_info(self):                 #SELF PARAMETRESINI OTOMATIK OLARAK ALIUYOR CUNKU BIR FONKS CAGIRICAZ VE BIR NESNE UZERINDEN CAGIRICAZ O DA O NESNEYI ICINE ALIYOR YANI SELF.
#         print(f"Ad:{self.name}  Soyad:{self.surname}  Yas:{self.age}")
#
#
#
#
#                                                             #SELF BIZIM OLUSTURUGUMUZ DEGISKEN OLUYOR. YANI ASAGIDAKI CALISAN1 SELF OLUYOR OTOMATIK ORAYA GONDERIYOR DEGERLERI.
# calisan1 = calisan("Ali", "Veli", 20)                  #BUARADA OLSUTURUGMUZ SINIFTAKI PARAMETLERI PARANTES ICINDE BEKLIYOR BIZDEN ONLARI GIRMEMIZ LAZIM.
# print(calisan1.name, calisan1.surname, calisan1.age)
#
# calisan2 = calisan("Mehmet", "Sarp", 16)        #ASLINDA BURADA CALISAN DEGISKENIM VAR VE BU OZELLIKLER (ATTRIBUTE) SUREKLI DEGISIYOR VE DIGER CALISAN1\2 DEGISKENLERINE AKTARILIYOR.
# print(calisan2.name,  calisan2.surname, calisan2.age)
#
# calisan1.show_info()            #BURADA ISE OLUSTURDUGUMUZ NESNEYLE CLASS ICINDEKI METODU CAGIRIYORUZ. VE BURADA CIKTILAR GELIYOR
# calisan2.show_info()            #HANGI DEGISKEN UZERINDEN BU FONKSIYONU CAGIRIRSAN SELF O NESNE OLUYOR VE O NESNENIN YAZMASINI ISTEDIGIN OZELLIKLERINI YAZIYOR.
                                #CUNKU USTTE SHOW INFO METOTU SELF PARAMETRESINI ICINE ALDIGI ICIN SELF PARAMETESI DE BIZIM NESNEMIZI TEMSIL ETTIGI ICIN HANGI NESNEYI YAZARSAK ONU ALIYORUZ


#NOT: EGER YUKARIDA INITTEN SONRAKI SELF I SILERSEN HATA ALIRSIN ALDIGIN HATA ISE SU SEKILDE OLUR CLASS SENDEN 3 TANE GIRDI ISTIYOR AMA SEN 4 TANE YOLLUYORSUN.
#BUNUN SEBEBI ISE CALISAN1 VE 2 NESNELERINI DE OZELLIK OLARAK ALIYOR CUNKU ONLARA ATAMA YAPIYOR. ONU ORADA KARSILAYAN DA SELF OLDUGU ICIN HATA VERMIYORDU AMA SILINCE BU HATAYI ALIYORUZ.





#\\\\\\\\\\\\\\\\\\\\\\\\\ NESNE OZELLIKLERININ BOS BIRAKILMA DURUMLARI ANLATIMI !!!!!!!!!!!!/////////////////////////////

# class calisan:
#     def __init__(self,name="girilmedi",surname="girilmedi",age=0):                      #BURADA AGE = 0 VERDIK CUNKU ASAGIDA AGE OZELLIGINE BIR DEGER GIRILMEZSE OTOMATIK OLARAK 0 ATAMASI YAPMASI ICIN...
#                                                                  #AYNISINI SURNAME VE NAME ICINDE YAPIYORUZ. DOLDUURLMASI ZORUNLU ALANLARA BU UYGULAMAYIYAPMIYORUZ KI DOLMADIGINDA HATA VERSIN.
#
#         #print("__init__ fonksiyonu calisiyor")
#
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
#     def show_info(self):
#         print(f"Ad:{self.name}  Soyad:{self.surname}  Yas:{self.age}")
#
#
#
# calisan1 = calisan("Ali",age=26)               #BURADA CALISAN1 NESNESININ OZELLIKLERINI BOS BIRAKIYORUZ VE DEFAULT DEGERLERI ATIYOR
#                           #BURADA ISE EGER SADECE TEK BIR DEGERIN GIRILMESINI VEYA BELLI BASLI BAZI OZELLIKLERIN GIRILMESINI ISTIYORSAK ONLARIN DEGERLERINI BOYLE ATIOYORUZ.
#                           #MESELE SURNAME I BOS BIRKATIK. EGER DIREK , 20 YAZSAYDIK BUNU SURNAME E ATICAKTI CUNKU SIRAYLA GIDIYOR,,.,.,,.!@#!@#
# calisan1.show_info()










#\\\\\\\\\\\\\\\\\\\\CLASS VERIABLES - INSTANCE VERIABLE////////////////// YANI SINIF DEGISKENLERI VE NESNELERIN DEGISKENLERI


# class calisan:
#
#     zam_orani = 1.1
#
#     def __init__(self,isim,maas):
#         self.isim = isim
#         self.maas = maas
#
# calisan1 = calisan("Ali", 5000)
# calisan2 = calisan("Veli", 8000)

# print(calisan1.__dict__)        #CALISAN 1 IN SAHIP OLDUGU OZELLIKLERI SOZLUK OLARAK DONDRUYOR....!!!!! DICT BUNA YARIYOR
# print(calisan2.__dict__)
# print(calisan.__dict__)       #BU ISLEMI DOGRUDAN CLASS ICIN DE YAPABILIYORUZ...!!!

# print(calisan.zam_orani)        #CLASS ICINDEKI DEGISKENE ERISEBILIYORUZ. BUNU CALISAN1 YANI NESNELERLE YAPARSAK DA ERISEBILIRIZ.

# print(calisan.__dict__)           #BURADA ZAM ORANINI GORUYORUZ CUNKU CLASS IN ICINDE
# print(calisan1.__dict__)        #AMA BURADA GOREMIYORUZ CUNKU NESNENINI ICINDE DEGIL AMA YINE DE ULASABILMEMIZIN SEBEBI KOMUTUN ONCE NESNEYI KONTROL ETMESI ORDA BULAMAZSA CLASS I KONTROL ETMESINDEN DOLAYI

# calisan.zam_orani = 1.2
# print(f"{calisan.zam_orani}\n{calisan1.zam_orani}\n{calisan2.zam_orani}")       #ZAM ORANI GUNCELLENDIGINDE OLUSTURULAN BUTUN NESNELERIN ZAM ORANLARI GUNCELLENIYOR HEPSI GUNCEL HALE GELIYOR.

# calisan1.zam_orani = 1.2        #BOYLE YAPTIGIMIZDA CALISAN1 NESNESININ ICINE ZAM_ORANI OZELLIGI EKLIYOR YANI ISIM VE MAAS OZELLIKLERININ YANINA ZAM_ ORANI BILGISI DE EKLENIYHOR.....
# # print(f"{calisan.zam_orani}\n{calisan1.zam_orani}\n{calisan2.zam_orani}")       #BURDA SPESIFIK OLARAK SADECE CALISAN 1 IN ZAM ORANINI DEGISTIRDIGIMIZ ICIN DIGERLERI AYI HALDE KALIYOR SADECE CALISAN 1 IN ZAM ORANINI DEGISTIRIYORUZ.
#
# print(calisan1.__dict__)        #BURADA YUKARIDA ZAM ORANI EKLEMESI YAPTIGMIZ ICIN OZELIKLERDE ARTIK YUKARIYA SELF.ZAM_ORANI EKLEMISIZ GIBI HAREKET EDIYOR ARTIK OZELIKLERDE GOZUKUYOR
#                                 #OZELLIGI KENDINDE BULDUGU ICIN DIREKT YAZDIRDI EGER BULAMASAYDI YUKARDAKI GIBI CLASSIN ICINE BAKACAKTI...
# print(calisan2.__dict__)        #CALISAN 2 DE BIR EKLEME YAPMADIGIMIZ ICIN GOZUKMUYOR.



#\\\\\\\\\\\\\\\\\\\\\\\\CALISAN SAYISI ARTTIKCA PERSONEL SAYISI ARTIRICAZ/////////////////////////////

# class calisan:
#
#     perseonel_sayisi = 0
#
#     def __init__(self,isim,maas):
#         self.isim = isim
#         self.maas = maas
#         calisan.perseonel_sayisi += 1       #HER NESNE URETILDIGINDE INIT FONKSOYNUNUN ICINE GIRILDIGI ICIN BURADA PERSONEL SAYISINI HER GIRILDIGINDE 1 ARTIRIYORUZ VE EKLENEN PERSONEL SAYISINI BULUYRUZ
#                                             #BURADA CALISAN.PERSONEL SAYISI YAPTIK CUNKU CLASS A AIT PERSONEL SAYISINI ISTIYORUZ. SELF . PERSONEL SAYISI YAPSAYDIK NESNEYE AIT BIR OZELLIK OLARAK ALIRDIK ONU ISTMEIYOURZ.
# print(calisan.perseonel_sayisi)         #ILK BASTA 0 OLARAK DEGER DONUDURUYOR CUNKU HIC NESNE URETILMEDI
# calisan1 = calisan("Ali", 5000)         #ILK NESNEMIZ URETILIYOR
# print(calisan.perseonel_sayisi)         #PERSONEL SAYIMIZ ARTIYOR....
# calisan2 = calisan("Veli", 8000)
# print(calisan.perseonel_sayisi)



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ CLASS METHODS , INSTANCE METHODS VE STATIC METHODS //////////////////////////////////

# class kisi:
#     zam_orani = 1.1             #BU ISE CLASS IN OZELLIGI YANI CLASS VERIABLE OLUYOR.!!!!
#     kisi_sayisi = 0
#     def __init__(self,isim="girilmedi",yas=0):    #BURADAKI ISIM VE YAS OZELLIKLERI INSTANCE VERIABLE DEGERLER YANI NESNENIN OZELLIKLERI CLASS IN OZELLIKLERI DEGIL
#         self.isim = isim
#         self.yas = yas
#         kisi.kisi_sayisi += 1
#
#     def bilgilerini_soyle(self):        #NESNEYE BAGLI METHOD YANI INSTANCE METHOD OLARAK GECIYOR BUNLAR. SELF E BAGLI SELF DE NESNELER ZATEN
#         return f"Isim: {self.isim}\nYas: {self.yas}"        #BURADA NESNENIN OZELLIKLERINI YAZDIIYORUZ ISIM VE YAS. BIR FONKSIYONA ATIYORTUZ YAZIRMA ISLEMINI
#                                                             #YANI BU BIR INSTANCE METHOD YANI NESNEYE BAGLI BIR METOD ICINE SELF ALIR SELFE YANI NESNEYE BAGLI METOD
#
#
#     @classmethod                    #CLASS METHOD OLUSTURUYORUZ ONUNU ICIN @CLASSMETHOD YAZMAMIZ GEREKLI, BUNU KULLANMAMIZ ICIN NESNE OLUSTURMAMIZA GEREK YOK..!!!!
#     def kisi_sayisini_soyle(cls):           #BURADA CLASS METHOD OLUSTURDUK ICINE OTOMATIK OLARAK CLS DEGERINI ALDI
#         return cls.kisi_sayisi
#
#
#
#
# kisi1 = kisi("Ali",30)
# kisi2 = kisi("Veli", 40)
# print(kisi1.bilgilerini_soyle())        #BURADA ISE YUKARIDAKI CLASS ICINDEKI FONKSIYONU NESNE UZERINDEN CAGIIRYORUZ VE CAGIRILAN NESNENIN OZELLIKLERINI BASTIRIYORUZ..


# print(kisi.isim)            #BURADA HATA ALIRIZ CUNKU KISI BIR NESNE OZELLIGI CLASS OZELIGI DEEGIL NESNE OZELLIKLERINE CLASS ILE ULASAMAYIZ.
# print(kisi1.zam_orani)      #AMA BURADA NESNE ILE CLASS IN OZELLIKLERINE ULASABILIYORUZ.        UFAK DETAY-/\-.

# print(kisi1.__dict__)
#print(kisi.kisi_sayisi)        #NESNENIN ICINE BIR DEGER GIRILMESE BILE DEFAULT ATADIGIMIZ DEGERLER ILE INIT FONK UN ICINE GIRDIGI ICIN KISI SAYISI YINE ARTIYOR YANI NESNE URETILIYOR.




#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ CLASS METHOD /////////////////////////////////////
# class kisi:
#     zam_orani = 1.1
#     kisi_sayisi = 0
#     def __init__(self,isim="girilmedi",yas=0):
#         self.isim = isim
#         self.yas = yas
#         kisi.kisi_sayisi += 1
#
#     def bilgilerini_soyle(self):
#         return f"Isim: {self.isim}\nYas: {self.yas}"
#
#
#
#     @classmethod                    #CLASS METHOD OLUSTURUYORUZ ONUNU ICIN @CLASSMETHOD YAZMAMIZ GEREKLI, BUNU KULLANMAMIZ ICIN NESNE OLUSTURMAMIZA GEREK YOK..!!!!
#     def kisi_sayisini_soyle(cls):             #BURADA CLASS METHOD OLUSTURDUK ICINE OTOMATIK OLARAK CLS DEGERINI ALDI
#                                                 #   BUARADAKI CLS DEGERINE KISI GELIYOR VE KISI_SAYISINI_SOYLE(KISI) OLUYOR BU DEGER
#         return cls.kisi_sayisi          #BURADA ISE KISI.KISI_SAYISI OLUYOR YANI KISI CLASSINDAN CEKIYOR FONKSIYONU
#
#
# kisi1 = kisi("Ali",30)
# kisi2 = kisi("Veli", 40)
#
# print(kisi.kisi_sayisini_soyle())       #KISI-SAYISINI_SOYLE PARAMETRESI ICINE PARAMETRE YAZMIYORUZ CUKU BASINDA KISI CLASS INDAN GELDIGINI BELIRTIYORUZ.
                                    #BURADA CLS PARAMETRESI ICINDE OLDUGU CLASS OLAN KISI CLASS INI ALIYOR. YANI BURADAKI CLS LER KISI OLUYOR AYNI USTTEKI SELF IN NESNE OLDUGU GIBI BURDA DA CLS CLASS OLUYOR

#\\\\\\\\\\\\\\\\\\\\\\BURADA HIC NESNE URETMESEK DE KISI SAYISINI SOYLE METODUNA ERISEBILIRIZ CUNKU CLASS IN ICINDE VAR OLAN BIR METOT BU.!!!! NESNE URETMEMIZE GEREK YOK ULASMAMIZ ICIN//////

#!!!!!!!!!!!!!!!ONEMLIII!!!!!!!!!!!!\\\\\\\\\\\\\\\\\\\NESNE URETMEDEN HERHANGI BIR FONKSYION CALISTIRMANIN EN BUYUK KULLANIM ALANI CONSTRUCTOR OLARAK KULLANMAKTIR..!!!!!
#CONSTRUSTOR ISE MESELA TOPLU BIR UYE KAYDI YAPACAKSIN TOPLU OLARAK STRING OLARAK DEPOLANMIS MESELA FARKLI FORMATTA DEPOLANMIS BUNU EKLEMEK ICIN TEK TEK ELLE YAZMAK YERINE
#BIR TANE FONKSIYONLA OTOMATIK OLARAK ISTEDIGMIZ FORMATA CEVIRECEK VE KISI CLASSINDAN NESNE URETMEYE YARIYOR. BUNUN GIB FARKLI FARKLI KULLANIM ALANALRI VAR BU ORNEK OLUYOR...!!!!!!!!!!!!!!!
#ASAGIDA O FONKSIYONU URETICEZ SIMDI///////////////////////////////////////////////////////////////////////////////////////////////////////////

# from datetime import date
#
# class kisi:
#     zam_orani = 1.1
#     kisi_sayisi = 0
#     def __init__(self,isim="girilmedi",yas=0):
#         self.isim = isim
#         self.yas = yas
#         kisi.kisi_sayisi += 1
#
#     def bilgilerini_soyle(self):
#         return f"Isim: {self.isim}\nYas: {self.yas}"
#
#
#
#     @classmethod
#     def kisi_sayisini_soyle(cls):
#         return cls.kisi_sayisi
#
# #\\\\\\\\\\\\\\\\\\\\\\\\FARKLI FORMATTAKI VCERININ SPLIT ILE BOLUNUP YENI NESNE URETILMESI//////////////////////////////////////////////
#
#     @classmethod                                 #YENI BIR CLASS METHOD ACIYORUZ FARKLI FORMATTAKI VERILERIN ISLENEBILME METODUNU URETMEK ICIN
#     def string_ile_olustur(cls,str_):           #YENI FONKSIYONUMUZU OLUSTURUYORUZ, ICINE STR_ OZELLIGINI EKLIYORUZ O OZELLIK BIZE GELEN FARKLI BICIMDEKI NESNELERIN YERINI TUTUCAK
#         isim,yas = str_.split("-")              #KISI CLASSINDAKI NESNELERIN OZELIKLERII BURAYA GIRIYORUZ VE STR_ NESNESININ - KARAKTEINE GORE BOLUNUP ILKININ ISIM DIGERININ YASA ATANMASINI YAPIYORUZ
#         return cls(isim,yas)            #ISIM VBE YASI CLS DEN RETURN EDIYORUZ CUNKU O DEGERLERE ULASMAMIZ LAZIM, BUNUN ICIN DE RETURN EDIYORUZ.
#
# #\\\\\\\\\\\\\\\\\\\\\\\\ISIM VE DOGUM YILI SEKLINDE GIRILMIS VERILERIN NESNESININ URETILMESI(YAS YERINE DOGUM YILI GIRILMIS ORNEK OLARAK...!!)//////////////////////////////////////////
#
#     @classmethod
#     def dogum_yili_ile_olustur(cls,isim,dogum_yili):        #BURADA 2 TANE OZELIK GIRIYORUZ CUNKU HEM ISIM VE HEM DOGUM YILINI AYRI AYI OZELLIK OLARAK VERIYOR BIZE VERI SETIMIZ. ONCEKINDE TEK BRI ONZELLIK ICINDE 2 TANE VERIYORTDU BZ AYIRIYORDUK BURDA FARKLI.
#         return cls(isim,date.today().year - dogum_yili)      #BURDAKI OLUSTURGUUMUZ YENI NESNEYI GERI DONDURMEK ICIN RETURN KULLANIYORUZ. KISI SINIFINDAN BIR NESNE OLUSTURUCAZ CLS DEDIK CUNKU KISI SINIFINDAN OLUSTURUCAZ..!!
#                                                             #DATETIME DATE KUTUPHANESINDEN BULUNDUGUMUZ YILI CEKIP ONDAN DOGUM YILINI CIKARTTIK VE SIMDIKIK YASINI BULDUK.
#
# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\STATIC METHOD OLUSTURMA VE KULLANIMI ////////////////////////
#
#     @staticmethod                   #STATIC METHOD KURUYORUZ..
#     def dogum_yili_hesapla(adam):                  #CLASSMETHODDA ICINE CLS DUZ METOTLARDA SELF ALIYOR AMA STATIC METHODDA BUNLARI ALMASI ZORUNLU DEGIL HICBISEY ALMAYADABILIR ALMAK ISTEDIGMIZI ALIYORUZ.
#         return date.today().year - adam.yas     #USTTE ICERIYE BIR DEGISKEN ATAMASI YAPIYORUZ STATIC METHOD ICINE, HERHANGI BIR DEGISKEN ISMI OLARBILIR MAKSAT ORADA TUTULMASI. OLDUGUMUZ YILDAN YASI CIKARTIP DOGUM YILINI BULUYORUZ.
#             #DIKKAT BURADA STATIC METHOD ICINE ISTEDIGIMIZ DEGISKENI YAZABILIRIZ MAKSAT ORADA TUTULACAK BIR DEGER OLMASI. NESNE ATAMASINI ZATEN ALT TARAFTA YAPIYORUZ KISI1 DIYE NESNE ATIYORUZ.
#     #/.////////////////////ISTERSEK BURAYA X KOYARIZ ISTERSEK Y KOYARIZ BUNUN KLASS ISMI OLMASINA GEREK YOK NESNE ISMI OLMASINA DA GEREK YOK!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# kisi1 = kisi("Ali",30)
# kisi2 = kisi("Veli", 40)
#
# kisi3 = kisi.string_ile_olustur("Ayse-25")          #BURADA YENI FORMATTAKI NESNEMIZI YENI CLASS METHODUMUZLA OLUSTURUYORUZ... VE YENI FONKSIYONUMUZ ONU - KARAKTERINE GORE BOLUYOR
# #print(kisi3.isim)                                   #BURADA ISLEMIN DOGRU SEKILDE YAPILIP YAPILMADIGNINI KONTROL EDIYORUZ
#
# kisi4 = kisi.dogum_yili_ile_olustur("Elif", 1990)       #BURADA YENI NESNEYI OLUSTUYUORUZ. BU SIRADA DOGUM YILI ILE OLUSTUR FONKSYIONU CAGIRILIYOR VE 1990 DAN BULUINDUGUMU ZENEYI CIKARTIP YASI BIZE BASTIRIYOR
# #print(kisi4.isim,kisi4.yas)
# print(kisi.kisi_sayisini_soyle())                   #NESNE GERCEKTEN URETILDI MI DIYE KONTROL EDIYORUZ.
# print(kisi.dogum_yili_hesapla(kisi2))           #STATICMETHODUMUZUN CALISIP CALISMADIGINI KONTROL EDIYORUZ.!!!!



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ NESNE TABANLI INHERITANCE   KATILIRIM  NEDIR NASIL KULLANILIR.!!!!!!!!!!!!!!!!!!!!!!!!////////////////////////////////////////

#BIR CLASSIMIZ OLUCAK VE ALT CLASLARIMIZ OLUCAK ALT CLASSLAR BAZI OZELLIKLERINI UST CLASSDAN ALICAK YANI. MESELA CALISAN DIYE BIR CLASS VAR ICINDE ISIM SOYISIM E MAIL VE MAAS OZELLIKLERI VAR
#BU CLASSIN ALTINA YAZILIMCI DIYE BIR CLASS OLUSTURUYORUZ CALISAN OZELLIKLERINE YAZILIMCI DA SAHIP CALISANDAN TUREDI CUNKU. MESELA MUDUR DIYE BASKA BIR CLAT CLKASS DAHA OLSUN ONLAR DA CALISAN
#OLDUGU ICIN CALISANDAKI OZELIKLER INTERITANCE ILE YANI KALITIM ILE DIGER CLASS A AKTARILIYOR..!!!! MESELA YAZILIMC CLASSINDA 2 TANE CLAS DAHA OLUSTURURSAK MESELA BACK END FRONT END DIYE
#BU BACKEND YAZILIMCIDAKI BUTUN OZELLIKLERE SAHIP FRONT END DE SAHIP YANI BIR USTUNUN OZELLIKLERINI ALIYOR BUNLAR.!!!! SADECE USTTEKI CLASTAN TURELILENLERE AKTARILMA OLUYOR.!!
#
# class Calisan:                          #DUMDUZ CLASS OLUSTUUYORUZ VE ASAGIDA OZELLIKLERI VERIYORUZ BURADA PARANTEZ YOK CUNKU HERHANGI BI YERDEN MIRAS ALMIYOR
#     zam_orani = 1.1
#     def __init__(self,isim,soyisim,maas):
#         self.isim = isim
#         self.soyisim = soyisim
#         self.maas = maas
#         self.email = isim + soyisim + "@sirket.com"
#
#     def bilgileri_goster(self):
#         return  "Ad: {} Soyad: {} Maas: {} Email: {}".format(self.isim,self.soyisim,self.maas,self.email)     #BURADA SELF FORMATIYLA ATAMALARI YAPIYORUZ RETURN ILE ICINDEKILERI DONDURUYORTUZ.!!
#
# calisan1 = Calisan("Ali","Caliskan",8000)
# calisan2 = Calisan("Veli","Klon",6700)
# #print(calisan2.email)
#
# #\\\\\\\\\\\\\\\\\\\\MIRAS ALAN CLASSA GELDIK ONU OLUSTURUYORUZ SIMDI////////////////////////////////
#
# class Yazilimci(Calisan):      #BURADA PARANTEZ VAR CUNKU MIRAS ALAN BIR CLASS BU..!!!!!!!!
#
#     def __init__(self,isim,soyisim,maas,bildigi_dil):
#         super().__init__(isim, soyisim, maas)       #SUPER BIZIM MIRAS ALDIGIMIZ CLASS I BELIRTIYOR.!!!
#                                                 #BURADA SUPER FONKSIYONU BIZE KOLAYLIKK SAGLIYOR SUPERDEN SONRA INIT ILE USTTELERI ALMAK YETERLI OLUYOR..!!
#                                             #BRUADA INIT EKLIYORUZ VE USTEKILERI HATA ALMAMAK ICIN USTTEKI OZELLIKLERI EKLIYORUZ. GENELLIKLE AYNI SIRADA EKLENIR USTTEKINE BILGILERI AKTARIM KOLAY OLSUN DIYE
#                                                  #BRUADA MESELA INIT YOKSA BURDA NESNE OLUSTURURKEN ILK GELYIOR BURAYA BAKIYOR INIT VAR MI. YOKSA MIRAS ALDIGI CLASS A GIDIYOR ORDAKI INIT OZELLLIKLERINI ALIYOR.
#                                                  #BOYLE DE NESNE OLUSTURABILIYORUZ.!!! YANI INIT OLMASI ZORUNLU DEGIL EGER IITY YOKSA USTTEKI CLASSDAN INIT OZELLIKLERIN CEKIYOR.!!!!
#
#         self.bildigi_dil = bildigi_dil
#
#
#
#     zam_orani = 1.2         #BURADA OVBERRRIDE VERIYOR CUNKU USTTEKI CLASIN USTUNE YAZIYORUZ.!!!!
#
#     def bilgileri_goster(self):     #AYNI SEKIL OVERRRIDE VERDI
#         return  "Ad: {} Soyad: {} Maas: {} Email: {} Bildigi Dil: {}".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
#
#     def dilini_soyle(self):
#         return f"Bildigi Dil: {self.bildigi_dil}"
#
#
# class Yonetici(Calisan):            #BIR YONETICI CLASSI OLUSTURUYORUZ BUNUN ALINA HANGI CALISANLARDAN SORUMLU FALAN ONALR GELICEK. CALISAN SILME CIKARMA EKLEME FALAN DA GELICEK.!!!
#
#     def __init__(self,isim,soyad,maas,calisanlar = None):       #SORUMLU OLDUGU CALISANLARI EKLIYORUZ
#         super().__init__(isim,soyad,maas)           #UST CLASSDAN OZELLIKLERI SUPERLE ALIYORUZ
#         if calisanlar == None:
#             self.calisanlar = []                #EGER CALISAN OZELIGI DOLDURULMAZSA NONE OLUP BOS LISTE KALMAYA DEVAM EDICEK
#         else:
#             self.calisanlar = calisanlar        #OYLE OLMAZSA ZATEN CALISANLAR OZELIGINE BIRISI EKLENMISTIR O DA BURADA EKLENIYOR SELF ILE.!!
#
#
#     def calisan_ekle(self,calisan):     #BU YONETICININ CALISANLAR LISTESINDE BIR CALISAN YOKSA O CALISANI CALISANLAR LISTESINE EKLIYOR.!!!
#         if calisan not in self.calisanlar:      #LISTEDE YOKSA EKLEYECEK VARSA HICBISEY YAPMAYACAK.!
#             self.calisanlar.append(calisan)
#
#     def calisan_sil(self,calisan):              #CALISAN SILME FONKSIYPONUMUZU OLSUTURYORUZ
#         if calisan not in self.calisanlar:      #EGER BOYLE BIR CALISAN YOKSA EKRANA UYARI YAZISI BASTIURIYOR.!!
#             print("Boyle bir calisan yok")
#         else:
#             self.calisanlar.remove(calisan)         #CALISANI KALDIRIYOR.!!!!
#
#     def calisanlari_goster(self):                   #CALISANLARI LISTELEME GOSTERIYORUZ
#         for calisan in self.calisanlar:                 #FOR DONGUSU ICINDE CALISAN DEGISKENI KULLANIM CALISANLAR LISTESINDEKILERIN OZELLIKLERINI BASTIRIYORUZ.!!
#             print(calisan.bilgileri_goster())
#
#
#
# yazilimci1 = Yazilimci("Ayse","Yildiz",7000,"Python")    #BURADA YAZILIMCI CLASS I ICINDE OLMAYAN OZELLIKLERI VEREBILIYORUZ CUNKU MIRAS ALDIGI CLASSDA BU OZELLIKLER VAR..!!!!!
#                                                 #BURADA INIT YOK OZELLIKLERI DIREKT MIRAS ALDIGI CLASSDAN YANI CALISAN CLASSINDAN CEKIYOR.!!! VARSA BURDAN CEKIYOR.!!!
# yazilimci2 = Yazilimci("Tayyib","Kaan",90000,"Full")       #NESNELERIMIZI OLUSTURUYORUZZ..!!!!!
# #print(yazilimci2.email)
#
# # print(calisan1.zam_orani)
# # print(yazilimci1.zam_orani)     #EGER YAZILIMCI ICINDE ZAM ORANI OLMASAYDI CALISANDAKI ZAM ORANINI ALICAKTI ONCE GELIYOR YAZILIMCIYA BAKIYOR VAR MI YOK MU DIYE YOKSA CALISANA GIDIYOR.!!
#
#
# #print(yazilimci1.bilgileri_goster())
# #print(yazilimci2.bilgileri_goster())        #ILK ONCE YAZIULIMCI CLASSINA BAKICAK BILGILERI GOSTERI BULAMAYINCA MIRAS ALDIGI CLASA GIDICEK.!!!
# # print(yazilimci2.dilini_soyle())
#
#
# #YONETICIYI URETTIGIMIZDE ALTINA CALISANLARI ILK BASTA EKLEMEDIK NONE OLARAK DONDURDUK ASSAGIDA CALISAN EKLE ILE CALISAN EKLEDIK..!!!
# yonetici1 = Yonetici("Ali","Kara","20000")
#
# # yonetici1.calisan_ekle(calisan1)                    #KENDISINE BAGLI OLARAK CALISACAK KISILERI EKLIYORUZ.!!!
# # yonetici1.calisan_ekle(yazilimci1)                  #EKLIYORUZ.!!!
# # yonetici1.calisanlari_goster()
# # print("********************")
# # yonetici1.calisan_sil(calisan1)
# # yonetici1.calisanlari_goster()
# # print("********************")
# # yonetici1.calisan_ekle(calisan1)
# # yonetici1.calisanlari_goster()
#
#
# #SIMDI YONETIYI URETIRKEN CALISANLARINI EKLIYORUZ DIREKT.!!!!!!...
#
# yonetici2 = Yonetici("Tk","I",473000000000,[yazilimci1,yazilimci2,calisan1])       #YUKARIDA BIZ CALISANLARI BIR LISTE YAPTIGIMIZ ICIN EKLERKEN DE LISTE OLARAK EKLIYORUZ.!!!  []
# # yonetici2.calisanlari_goster()
#
# #\\\\\\\\\\\\\\\\\\\BIR SINIF BIR SINIFIN ALT CLASSI MI YOKSA ONDAN URETILMIS BIR NESNE MI ONUN AYRIMINI KONTROL ETMEYI GOSTERIYORUZ..!!!!/////////////
#
# # print(isinstance(yonetici2,Calisan))        #CIKTI OLARAK TRUE ALDIK BU DA DEMEK OLUYOR KI YONETICI2 BIR CALISANDIR YANI CALISAN CLASSINDAN URETILMIS BIR ORNEKTIR!!!.
# # print(isinstance(yonetici2,Yazilimci))      #FALSE CIKTIISNI ALDIK CUNKU YONETICI YAZILIMCI CLASSINDAN URETILME DEGIL
# # print(isinstance(yazilimci2,Yazilimci))     #BURADA TRUE CIKTI CUNKU YUAZILIMCI2 YAZILIMCI CLASSINDAN URETILEN BIR NESNEDIR.!!!!!
#
# #YANI ISINSTANCE KOMUTU 1. YAZDIGIMIZ 2. YAZDIGIMIZDAN MI URETILME BUNU SOYLUYOR BIZE.!
#
#
# #\\\\\\\\\\\\\\\\\\\BU ISE BU CLASS BU CLASSIN ALT CLASSI MI ONDAN MI TURETILDI ONU DONDURUYOR.!!!/////////////////
#
# print(issubclass(Yazilimci,Calisan))        #TRUE DONDURDU CUNKU YAZILIMCI CALISAN CLASSININ BIR ALT CLASSI ONDAN URETILMISTIR
# print(issubclass(Yonetici,Yazilimci))       #FALSE CIKTI CUNKU YONETICI YAZILIMCI CLASSINDAN URETILMEDI.!!









































