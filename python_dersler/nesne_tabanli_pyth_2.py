# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ DUNDER METHOD (MAGIC METHODSSS) NESNE TABANLI BOLUM 2 ///////////////////////////////////////
# ISMININ DUNDER OLMASININ SEBEBI 2 TANE ALT TIREYLE BASLIYOR OLMALARI BU KOMUTLARIN.!! UNDER SCORE YANI DOUBLE UNDERSCOPE YANI DUNDER.


# \\\\\\\\\\\\\\\\\\\\\__ADD__ METHODU///////////////////////////
# print(3 + 5)        #BURADA PYTHON ONCE VERININ TIPINE BAKTI. INTEGER BIR DEGER GRDU VE INTEREGERDAKI ADD METODUNU CAGIRDI ASLINDA.
# print(int.__add__(3,5))        #ASLINDA OLAN SEY ISE BU =  INT TAMSAYI CLASSINI ISMI. INT CLASSININ ICINDEKI ADD CLASORUNU CAGIRDI ONA 3 VE 5 I GONDERDI VE CIKTIMIZ 8 OLUYOR ASLINDA BUNU YAPIYOR
#
#
# print("Ali" + "Veli")       #BURDA DA STRING OLDUGUNU GORDU STR ICINDEKI TOPLAMA FONKSIYONUNU CAGIRDI
# print(str.__add__("Ali","Veli"))        #ARKA TARAFTA BUNU DONDURUYOR YANIU
#
#
# print([1,2,3] + [4,5,6])        #BURDA DA LISTE OLDUGNU GORDU
# print(list.__add__([1,2,3],[4,5,6]))    #BUNU DONDURDU
#
# #ADD METHODU HER CLASS ICIN AYRI AYRI TANIMLANMIS. YANI TOPLAMA YAPARKEN ASLINDA ADD METHODUNU KULLANIYORUZ..!!!!!!!


# class Mylist(list):  # LIST DEN MIRAS ALIYOR YANI LISTEDEN URETILMIS BIR CLASS OLUSTURUYORUZ BURDA
#
#     def __add__(self, other):  # ILK ONCE HANGI NESNEMI GONDERIRSEM O SELF DIGERI ISE OTHER OLUYOR..!! # TOPLAMA ISLEMI ICIN YAPTIGIMIZ ISLEMLER
#         if len(self) != len(
#                 other):  # BURADAKI YAPACAGIMIZ LISTELERIN ILK ONCE 0. ELEMANLARI TOPLANACAK SONRA 1 2 DIYE GIDECEK UZUNLUKLAR AYNI DEGILSE TOPLANMAYACAL.!  SELFIN UZUNLUK OTHERINKINE ESIT DEGIL ISE
#             return "Bu elemanlar toplanamaz."  # UZUNLUKLAR AYNI OLMADIGI ICIN TOPLANAMAZ
#         else:
#             result = Mylist()  # MYLIST CINSINDEN YANI CLASS IN CINSINDEN BIR NESNE OLUSTUUYORUZ BURDA DA. BU CLASSIN CINSINDEN BIR NESNE OLMASI LAZIM YANI MANTIKEN
#             for i in range(len(self)):
#                 result.append(self[i] + other[i])
#             return result  # EVET SONUC OLARAK ISTEDIGIMIZ SEYI BASTIRDI. 1 LE 4 U TOPLADIU 5 ETTI. 5 VE 2 YI YOPLADI 7 ETTI. 3 VE 6 YI TOPLADI 9 ETTI.!!
#
#
# #///////////////////SUB KULLANIMI YANI CIKARMA ISLEMI MTODUNUN KULANIMI!!!!!!!\\\\\\\\\\\\\\\\\\\\\\
#     def __sub__(self, other):       #CIKARMA ISLEMI ICIN YAPACAGIMIZ ISLEMLER. LIST OPERATORUNDE TOPLAMADAKI GIBI DOHGRUDAN - ILE CIKARMA YAPAMITYORUZ HATA ALIRIZ.!!
#         if len(self) != len(other):  # BURADAKI YAPACAGIMIZ LISTELERIN ILK ONCE 0. ELEMANLARI CIKARACAK SONRA 1 2 DIYE GIDECEK UZUNLUKLAR AYNI DEGILSE CIKARMAYCAAK.!  SELFIN UZUNLUK OTHERINKINE ESIT DEGIL ISE
#             return "Bu elemanlar cikarilamaz."  # UZUNLUKLAR AYNI OLMADIGI ICIN TOPLANAMAZ
#         else:
#             result = Mylist()  # MYLIST CINSINDEN YANI CLASS IN CINSINDEN BIR NESNE OLUSTUUYORUZ BURDA DA. BU CLASSIN CINSINDEN BIR NESNE OLMASI LAZIM YANI MANTIKEN
#             for i in range(len(self)):
#                 result.append(self[i] - other[i])
#             return result
#
#
# #\\\\\\\\\\\\\\\\\\\\\ESIT MI DEGIL MI ONA BAKICAZ SIMDI DE//////////////////////
#     def __eq__(self, other):        #BURADA TOPLAMLARININ ESITLIGINI KONTROL ETMEK ICIN __EQ__ KOMUTUNU KULLANIYORUZ BU DISARIYA ESIT MI DEGIUL MI BAKMAMIZI SAGLAYACAK.!!!
#         if sum(self) == sum(other):     #EGER TOPLAMLAR ESITSE
#             return True             #TRUE DEGERINI DONDURECEK
#         return False                #ELSE KULLANMADIK CUNKU ZATEN EGER ICERI GIRERSE TRUE DONDURECEK GIRMEZDE DIREKT FALSE DONDURECEK.!!!
#
#
# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\MUTLAK DEGERE CEVIRICEZ SIMDI !!!!!!!!!!!!!!!!!!!!!/////////////////////////////
#
#     def __abs__(self):      #ABS ILE MUTLAK DEGERI YAPOMASI ICIN GEREKLI METHODU EKLIYORUZ
#         result = Mylist()       #BURADA MYLIST CESIDINDEN YANI LISTE CESIDINDEN BIR DEGISKEN OLUSTURUYORUZ
#         for i in self:          #FOR DONGUSUYLE ICINDEKI PARAMETREYI ALIYORUZ YANI SELFI SELF DE BIZIM LISTELERIMIZI TEMSIL EDIYOR
#             if i >= 0:              #FOR DONGUSU ICINDEKI I SIFIRDAN BUYUKSE ZATEN MUTLAK DEGER ALINACAK BISEY YOKTUR ONU OTOMARIK OLARAK RESULT DEGISKENINE EKLIYORUZ
#                 result.append(i)        #RESULT DEGISKENINE APPEND YONTEMI KULLANARAK EKLEDIK.!
#             else:                       #ELSE DURUMUNDA YANI SAYININ SIFIRDAN KUCUK OLDUGU NEGATIF DURUMLARDA ISE
#                 result.append(-1*i)         #SAYISI -1 LE CARPIP YANI POZITIF HALE GETIRIP RESULT LISTESINE APPEND EDIYORUZ YANI EKLIYORUZ
#         return result               #RESULT LISTESINI RETURN EDIYORUZ CUNKU DISARIDAN RESULT DEGISKENINE ULASABILELIM DIYE. RETURN ETMEZSEK ULASAMAYIZ VE BIR CIKTI ALAMAYIZ.!!!
#
# liste1 = Mylist([1, 2, -3])
# liste2 = Mylist([-4, 5, -6])
# #
# # Toplama işlemi (other da Mylist nesnesi)
#            #liste nesnelerini burada mylist ile olusturup add fonksiyonuna atadigimiz icin burada kullandigimizde toplamay izin veriyor(normalde de toplaniyor cikarma olmuyor)
# print(liste1+liste2)  # [5, 7, 9]
#
# # Çıkartma işlemi (other da Mylist nesnesi)     #BURADA ISE MYLIST ILE OLUSTURDUGUMUZ ICIN __SUB__ FONKSIYONU ICINE LISTELERIMIZIN ATAMALARI GERCEKLESTIGI ICIN ARTIK LISTE1 VE LISTE 2 NESNELERIMIZDE CIKARMA ISLEMINI YAPABILIYORUZ...!!
#                  #\\\\\\\\yani bizim liste1 ve liste2 nesnelerimiz mylist classi icinde __sub__ metoduna atandigi icin cikarma islemini yapabiliyoruz.///////!!!!
# print(liste1-liste2)  # [-3, -3, -3]
#
# #TOPLAMLARI BIRBIRINE ESIT MI DEGIL MI ONU KONTROL EDIYORUZ.!!!
# print(liste1 == liste2)     #FALSE DEGER DONDURDU TOPLAMLAR BIRBIRINE ESIT DEGIL.!!!
#
# #MUTLAK DEGER DONDURMA
# print(abs(liste1))          # abs degerinin icine liste4 yaziyorum ve selfe otomatik olarak liste4 un atamasini yapiyor ve liste 4 icindeki sayilari for dongusundeki i sayesinde
# print(abs(liste2))          #sifirdan buyukse aynen yazip sifirdan kucukse -1 le carpip tekrardan listeye ekliyor yani







#\\\\\\\\\\\\\\\\\\\\\\\\\\\ FARKLI KULLANIM ORNEGI///////////////////////////////
# class Mylist (list):
#
#     def __sub__(self, other):
#         if len(self) != len(other):
#             return "Bu elemanlar cikarilamaz."
#         else:
#             result = self[:]
#             for i in range(len(self)):
#                 result[i] = self[i] - other[i]
#             return result
#
#     def __add__(self, other):
#         if len(self) != len(other):
#             return "Bu elemanlar toplanamaz."
#         else:
#             result = self[:]
#             for i in range(len(self)):
#                 result[i] = self[i] + other[i]
#             return result
#
#
# liste1 = Mylist([1, 2, 3])
# liste2 = Mylist([4, 5, 6])
#
# print(liste1 - liste2)
# print(liste1 + liste2)




#\\\\\\\\\\\\\\\\\\\\\\\\\ SIMDI LIST CLASSINDAN CIKIP KENDI OZELLIKLERI OLAN BIR CLASSIMIZI ACIYORUZ //////////////////////////////////////////////////  FARKLI ISLEMLER YAPICAZ....!!!!/////
#
# class Futbolcu:
#     def __init__(self,isim,soyisim,yas):
#         self.isim = isim
#         self.soyisim = soyisim
#         self.yas = yas
#
# #NENELERIN ESIT OLUP OLMADGINI KONTROL ETME
#     def __eq__(self, other):
#         if self.isim == other.isim and self.soyisim == other.soyisim:       #FUTBOLCULARIN ISIMLERI VE SOYIISMLERI AYNOIYSA TRUE DONDURECEK
#             return True
#         return False
#
# #TOPLAMA YAPMA
#     def __add__(self, other):
#         A = self.isim[0] + other.isim[0]            #ISIMIN ILK HARFLARI TOPLAMI
#         soyisim = self.soyisim[0] + other.soyisim       #SOYISMIN ILK HARFLERI TOPLAMI
#         yas = self.yas + other.yas                      #YASLAR TOPLAMI
#         return Futbolcu(A,soyisim,yas)       #GERIYE YENI BIR NESNE OLUSTURUYORUZ YANI FUTBOLCU CLASSINDAN YENI BIR NESNE OLUSTUUYORUZ BU YUZDEN DE FUTBOLCUYU RETURN EDIYORUZ
#                                                 #YENI NESNENIN ISIM SOYISIM VE YASLARINI YENI NESNENIN OZELLIKLERINE YASIYORUZ ONLAR DA USTTEKI YAZDIGMIZ METODUN ICINDEKI YAZANLAR ZATEN
#                                                 # GORDUGUN GIBI ORALARA MESELA ISIM YERINE A DA YAZBIIRIZ ORASI BIZIM KOYDUGUMUZ DEGIUSKEN DIGERI CLASSIN OZELLIGI OLUYOR. CLASS OZELLIGINII DEGISKENE ATIYORUZ
#
# #BUYUKLUK KUCUKLUK BAKIYORUZ BURADA LT KUCUKTUR GT ISE BUYUKTUR FONKSIYONLARINI KULLANMAMIZI SAGLIYOR.!!!!!!
#     def __lt__(self, other):                #BUYUKTUR KUCUKTUR KOMUTNU YAPTIRTIYPORUZ
#         if self.yas < other.yas:                #IFLI EKLIYORUZ
#             return True                 #KUCUKSE TRUE
#         return False                #DEGIULSE FALSE
#
# futbolcu1 = Futbolcu("Yalcin","Turan",32)       #NESANELER OLUSUYOR
# futbolcu2 = Futbolcu("Hakan","Unal",25)
#
# #!!!!! TOPLAYABILIYORUZ AMA DIREK PRINT EDRSEK ISTEDIGIMIZ CIKTIYI ALMIYORUZ. ONU ALMAK ICIN AYRIYETEN STR METODUNU KULLANMAMIZ GEREKIYOR. BOYLE OLUNCA DIREK YAZDIRMAZ SONUNA OZELLIK EKLEME YAPMAMIZ GEREKIYOR BOYLE YAZDIRMAK ICIN.
# futbolcu3 = futbolcu1 + futbolcu2       #FUTBOLCU 1 ILE FUTBOLCU IKIYI TOPLAYABILIYORUZ ARTIK
# print(futbolcu3)                        #CIKTIDA FUTBOLCU NESNESI DIYIP HAFIZADA BULUNDUGU ADRESI GOSTERIYOR.!!
# print(futbolcu3.isim)                       #BURADA CIKTIMIZ YH OLDU. EGER BOYLE TEK TEK ISIM SOYISIM YAS DEGISKENLERINI PRINE VERIRSEK ISTEDIGIMIZ CIKTIYI ALABILIYORZ
#
# print(futbolcu1 == futbolcu2)       #FUTBOLCULAR NESNELERININ ISIMLERI VE SOYISIMLERI BIRBIRINE BIR MI. BIR ISE TRUE DEGILSE FALSE DONUYOR.
#
# print(futbolcu1 > futbolcu2)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\COOOOOOOOOOOOOOOOOOK ONEMLI BILGI!!!!!!!!!!!!!!!! SELF VE OTHER LISTEDEKI HER ELEMANIN ISIM VE SOYISIM OZELLIKLERININ ILK HARFLERINI TOPLAMAZ SADECE ILK VE SON ELEMANIN ILK HARFLERINI TOPLAR
# //////////////////////////////////ONUUN ICIN AYRI BIR FONKSIYON KULLANMAMIZ GEREK O DA SOYLE////////////////////////
#   AYNI CLASS ICINDE BIR FONKSIYON OLUSTUURP ONUNLA TOPLUYORUZ
# class Futbolcu:
#     def __init__(self, isim, soyisim, yas):
#         self.isim = isim
#         self.soyisim = soyisim
#         self.yas = yas
#
#     @staticmethod
#     def toplam_veriler(futbolcular):
#         isim_ilk_harfleri = ""
#         soyisim_ilk_harfleri = ""
#         yaslar_toplami = 0
#
#         for futbolcu in futbolcular:
#             isim_ilk_harfleri += futbolcu.isim[0]
#             soyisim_ilk_harfleri += futbolcu.soyisim[0]
#             yaslar_toplami += futbolcu.yas
#
#         return isim_ilk_harfleri, soyisim_ilk_harfleri, yaslar_toplami
#
#
# # Futbolcuları bir listeye ekliyoruz.
# futbolcular = []
# futbolcular.append(Futbolcu("Yalcin", "Turan", 32))
# futbolcular.append(Futbolcu("Hakan", "Unal", 25))
# futbolcular.append(Futbolcu("Ahmet", "Yılmaz", 28))
# # Diğer futbolcuları da aynı şekilde ekleyebilirsiniz.
#
# # Tüm futbolcuların ilk harflerini, soyisimlerini ve yaşlarını topluyoruz.
# isimler, soyisimler, yaslar = Futbolcu.toplam_veriler(futbolcular)          #BUARADA USTEKI ISIM_ILK_HARFLERI GECICI DEGISKENININN DEGERINI ISIMLER ADLI DEGISKENE ATIYORUZ, BURADA SIRAYLA GIDIYORUZ

# #ILK ONCE ISIMLER YAZIYORUZ TOPLAM VERILERIN ILK ALTINDAKI ILK GECICI DEGISKEN BU OLUYOR SONRA SOYISIM SONRA YASLARA ATAMALARI SIRAYLA YAPIYORUZ/
# #ISTERSEK BURDA DEGISKENLERE ISIMLER SOYIISMLER DEGIL A B C FALAN DA DIYEBILIRDIK YANI SORUN YOK.!!
#
# # Toplam verileri ekrana yazdırabilirsiniz.
# print("Toplam İlk İsim Harfleri:", isimler)
# print("Toplam İlk Soyisim Harfleri:", soyisimler)
# print("Toplam Yaşlar:", yaslar)





#\\\\\\\\\\\\\\\\\\\\\\\\\\\!!!!!!!!!!!!!!!!!!__str__ ve __repr__ METODLARININ KULLANIMLARI  MAGICLER DEVAMMQEEE!!!!!!!!!!!!!!!!!!!!!!///////////////////////////////
#BUNLARIN YAPTIGI IS CLASSDAN URETILEN NESNENIN NASIL STRINGE DONUSTURULECEGI BUNLARIN GOREVI.!!
#YANI YAZDIR DEDIGMIZDE EKRANA NASIL YAZILACAGINI BELIRLEYEN IKI TANE FONKSYION BIRBIRLERINE BAZEN COK BENZESELERDE AYUNI FONKSIYON DEGILLER!!!
#FARKLARI VE NASIL KULLANILDIKLARI !!!!!!!!!!


# a = "mevsimler gecerken temmuz gelir giderken. o yesil gozlerinde ben yoktummmmmmm."
# print(str(a))       #BURADA DIREK YAZDIRIYOR PYTHONU
# print(repr(a))      #AMA BURADA BUNUN BIR STR OLDUGUN BELIRLETEN 2 TANE TIRNAK ILE YAZDIRIYOR.!!!!! YANI STR OLDUGUNU BELLI EDIYOR.!!!!!


# b = 2/11            #BURADA BIR FARK GOREMIYORUZ
# print(str(b))           #AYNI CIKTILAR VERIULIYOR
# print(repr(b))

#//////\\\\\\\\\!!!!! SIMDIIII EN CAN ALICI ORNEK GELIYOR\\\\\\\\\\\\\\\\\\\\\\\\\\

# from datetime import date
# import datetime

# bugun = date.today()
# print(bugun)
# print(str(bugun))           #CIKTILAR NORMAL PRINTLE AYNI OLUYOR BURDA.!!
# print(repr(bugun))          #EVET BURADA HANGI OBJE OLDUGNU SOYLUYOR MESELA BURADA DATETIME.DATE OBJESIDIR BU DIYOR BURADA FORMAT DA DEGISIYOR VE ICINE ALDIGI PARAMETRELER BUNLARDIR DIYE PARANTEZ ICINDE GOSTERIYOIR

#YANI IKSIIDNIN ARASINDAKI FARK
#STR FONKSYIONU KULLANICININ GORMESINI ISTEDIGMIZ CIKTIYI GOSTERIYORUZ MESELA SADECE TARIHI GORMESI ICIN
#REPR ISE YAZILIMCININ KENDISININ GORMESI ICIN GEREKLI MESELA DEBUG YAPARKEN YA DA NE NESNESI OLDUGUN GORMEK ISTERKEN KULLANILIR BU

#c = datetime.date(2023, 9, 3)       #MESELA BURADA REPR IN CIKTIGINI KOPYALAYIP YAPISTIRINCA BU NESNE UZERINDE DEGISIKLIK YAPABILIRIM. YANI GELISTIRICI ICIN ONEMLI



#EGER BIZ BIR SEYI DUMDUZ PRINT ILA YAZDIRACAKSAK PRINT ONCE CLASS ICINDE STR YE BAKIYOR VARSA YAZDIIYOR YOKSA REPR YE GIDIYOR/ SIMDI BUNUN ORNEKLERINI YAPALIM!..


# class Futbolcu:
#     def __init__(self,isim,soyisim,yas):
#         self.isim = isim            #SAGDAKILER FONKSYIONDAN GELENLER YANI USTTEKILER SAGDAKI OLUYOR ISTERSEK A B C DERIZ SELF. OLANLAR ISE SONRADAN VERECEGIMIZ DEGISKENLER
#         self.soyisim = soyisim
#         self.yas = yas
#
#     def __str__(self):                          #EVET
#         return f"ad: {self.isim} soyad: {self.soyisim} yas: {self.yas}"     #BURADA ISTERSEK YAS I YAZDIRMAYIZ HERHANGI BIR HATA VERMEZ HANGISINI GOSTERMEK ISYIRTOSAK ONU YAZARIZ.!!
#
# #BURASI REPR NIN DUZGUN OLMAYAN SADECE GOTERIMLIK ICIN YAZDIGIMIZ KISMIYDI SIMDI GERCEK KULLANIMLARINDAN BRIISNE YAANI NESNENIN OZELIKLERINE ULASMAK ICIN KULLANCAGIMIZ HALINI YAZICAZ
#     #def __repr__(self):                   #EGER STR FONKSIYONUMUZ OLMAZSA VEYA ONU YORUM SATIRINA ALIRSAK BURADA PRINT FONKSIYONUMUZ YUKARIDAKI CLASS ICINDE STR BULAMAYACAK VE
#         #return "Repr calisiyor..!!"             #REPR FONKSIYONU ICINE GIRIP ONU CALISTIRACAK YANI ONCELIK REPR FONKSIYONUNDA DEGIL STR FONKSIYONUNDA OLUYOR PRINT ISLEMINDE.!!!!
#
#
# #BURASI REPR NIN OLASI NORMAL KULLANIMI ICIN YAZDIGIMIZ ORNEK OLACAK.!!!! YANI NESNEYI BASTAN URETME ICIN KULLANICAMIZ ISLEVI
#     def __repr__(self):
#         return f'Futbolcu("{self.isim}","{self.soyisim}",{self.yas})'     #EGER BURADA HEPSINI CIFT TIRNAK ILE YAPARSAK KIRMIZILIKLAR ILE HATA VERICEK VE 2. CIFT TIRNAKTA BITTIGNI SANICAK O YUZDEN
#                                                     #DIS TARAFTAKI F STRINGININ TIRNKLARINI TEK TIRNAK YAPIYORUZ.!! DIKKAT ET BUNA.!!!
#         #BURANIN CKTISI TAM ISTEDIGMIZ GIBI NESNENIN OLUSTURULMA ESNASINDAKI GIBI  CIKIYOR YANI BOYLE : Futbolcu("Hakan","Unal",20) ISTEDIGMIZ BU BIZIM NESNEYI DUZENLEMEK ICIN.!!
#
# futbolcu1 = Futbolcu("Hakan","Unal",20)     #NESNEYI OLUSTURUYORUZ
#
# print(futbolcu1)                #!!!!!!!!!!!!!!!!!/\/\BU YAZDIKLARIM DEF __STR__ FONKSIYONU YAZILMADNA ONCESI ICIN GECERLI/\/\!!!!!!!!!!!!!!!!!!!!!!!!!!
#  #BOYLE YAZDRIDIGMIZDA BEKLEDIGMIZ GIBI BIR CIKTI ALMIYORUZ CLASS ADI HANGI CLASSIN NESNE OLDUGU VE KAYDEDILDIGI YERI BANA GOISTERIYOR.
# #CLASS ICINE BAKTI STR FALAN GOREMEDI O YUZDEN BEN BOYLE YAZDIRIYORUM DIYE NESNENIN OZELIKLERINI YAZDIRDI.!!! YANI NE OBJESI OLDUGU VE ADRESINI YAZDIRDI.!!
# #DONUP STR YI BULURSA EGER BIZIM ISTEDIGMIZ FORMATTAKI YAZIYI YAZDIRIR.!!
#
# print(repr(futbolcu1))          #EGER BOYLE YAPARSAK DEFAULT HALI NORMAL STR YAZDIRMAK YERINE BIZ REPR DE CALISTIRMASINI SOYLEDGIMIZ ICIN STR YI ES GECIP REPR FONKSIYONU ICINE GIRIP ONU YAZDIRACAK
# #print(futbolcu1.__repr__())     #BU DA USTTEKI ISLEMIN AYNISINI YAPIYOR SADECE FORMAT DEGISIYOR!!!...!!
#
#
# #BRUADA REPR CIKTISINDAN DEN ELDE ETTIGMIZ NESNEYI KOPYALIYORUZ VE YENI BIR NESNE OLUSTURUYORUZ VEYA DUZENLIYORUZ.!!
# futbolcu2 = Futbolcu("Is insani","Ali Bey",40)


#YANI ISIN OZU SU DUZ STR SON KULLANICIYA YA DA GORUNMESINI ISTEDIGIMIZ GIBI YAZDIRILMASI ICIN KULLANDIGIMIZ BIR FONKSIYON AMMMAA
#REPR ISE BIZ BUNUN CLASSINA OZELLIKLERINE BAKICAZ FALAN DERSEK REPR KULLANMAMIZ GEREKIYOR.!! NESNENINE OZELIKLERINE ULASIP DEGISIKLIK YA DA EKLEME YAPMAK ICIN!!!





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\!!!!!!!!!!!!!!!!!if __name__ == "__main__" Kalıbı KULLANIMLARIIIIIIII!!!!!!!!!!!////////////////////////////////

#MAGIC METODLARLA ALAKALI BIR KONU OLAN if __name__ == "__main__" YAPISI NEDEN VAR NEDIR?

# import modul2       #BU IMPORTUN KULLANIMI MESELA BIZ BASKA BIR DOSYAYA CESITLI FONKSIYONLAR YAZIYORDUK VE ONLARI KULLNAMKA ISTIYORSAK O DOSYAYI IMPORT EDIYORDUK.!!!
#
# print("Birinci Modulun Ismi " + __name__)       #BURADA DIREK OLARAK CALISTIRMAYI BURADAN YAPARSAK MAIN OLAN KISIM CALISTIRIGMIZ KISIM OLACAK VE IMPORT ETTIGIMIZ MODUL2 ISE DIREK DOSYANIN ADINI ALICAK YANI BURADA MODUL2 ADINI ALIYOR.!!!!!
# #PYTHON DIREKT OLARAK CALISTIRILAN DOSYANIN ISMINI MAIN OLARAK AYARLIYOR .////DIREKT OLARAK CALISTIIRLAN DOSYANIN ISMI MAIN OLUYOR.!


#\\\\\\\\\\\\\\\\\\\\\\\\!!!!!!!!!!!!!!! SIMDI GELELIM BU IFADE NEDEN VAR NEDEN if __name__ == "__main__" DIYORUZ NEDEN VAR BU? !!!!!!!!!!!!!!!!!!//////////////////////////////

#BURANIN ALTINDAKILER MODUL2 DOSYANSININ ICINDE OLMASI GEREKENLER ORADAN ALDIGMIZ SADECE NEDENINI ANLATMAK ICIN KOYDUM YOKSA BUNLARIN YERI BURASIU DEGIL.!!

# #__NAME__ METODU ICIN DEME YAPILDI SADECE.!! NESNE TABANLI 2 DE ANLATIMI VAR!.
#
# if __name__ == "__main__":      #BURAYA BOYLE BIR KALIP KULLANIYORUZ MODUL2 DOSYAMIZA .!!!!
#     print("Ikinci Modulun Ismi " + __name__)        #BOYLE OLDUGU ZAMAN EGER + __NAME__ KALIBINI DIGER DOSYADA CALISTIRIRSAK BURDAKI ARTIK IKINCI MODUL ISMI MODUL2 YAZMAYACAK SADECE
#                                             #__MAIN__ YANI NEREDE CALISTIRILDIYSA O YAZACAK TEK BIR SATIR OLACAK BUNNU SEBEBI ISE
#                                         #__MAIN__ OLARAK YANI CALISTIRLAN YER OLARAK BIZ BURAYI KULLANMADIK O YUZDEN BURASI YAZDIRILMIYOR.
#                                         #YAZDIRILMAMA SEBEBI ISE PRINT KOMURUNU IF KOSULUNUN ICINDE EGER SADECE BU SAYFANIN ISMI YANI + __NAME__ I __MAIN__ ISE YAZDIR YOKSA BIR SEY YAPMA DEMEMIZ.
#                                         #EGER BURDAN CALISTIRIRSAK CALISIR VE IKINCI MADULUN ISMI __MAIN__ OLUR.!!!




#\\\\\\\\\\\\\\\\\\\\\\\!!!!!!!!!!!!!!!!! SIMDI GELELIMM BU KALIBIN ORNEK KULLANIMLARINA !!!!!!!!!!!!///////////////////////

# import modul2
#
# print("Birinci Modulun Ismi " + __name__)
#
# #EGER MODUL2 DEKI FONKSIYONA ULASMAK ISTIYORSAK TABIKI DE ULASIRIZ CUNKU MODUL2 YI IMPORT ETTIK SOYLE ULASABILIRIZ.
#
# modul2.fonksiyon()              #BOYLE BULUNDUGU DOSYANIN ISMINI VE CAGIRMAK ISTEDIGIMIZ FONKSIYONUN ISMINI YAPARAK ULASABILIRIZZZZ.!!!!









































