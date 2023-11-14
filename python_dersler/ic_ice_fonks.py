#ic ice birden fazla fonksiyon koymamizla olusur. ornek olarak:

# def dis_fonk():
#     print("Dis Fonksiyon Calisiyor")
#     def ic_fonk():
#         print("Ic Fonksiyon Calisiyor")         #bu durumda ic fonksiyon calismayacaktir, cunku icinde oldugu fonksiyonda ic fonksiyonu cagirmadik
#     print("Dis Fonk Sonlaniyor")                #buranin ciktisi sadece dis fonksiyon calisiyor ve dis fonk sonlaniyor olacaktir cunku ic fonku cagirmadik
#
# dis_fonk()
#
#
# def dis_fonk():
#     print("Dis Fonksiyon Calisiyor")
#     def ic_fonk():
#         print("Ic Fonksiyon Calisiyor")
#     print("Dis Fonk Sonlaniyor")
#     ic_fonk()                                       #buradaki gibi ic fonksiyonu cagirirsak eger dis fonksiyonun icinde o zaman ekrana yuazdiracaktir (cagirildigi yerde)
#
# dis_fonk()



#Simdi bunu parametreli sekilde yapacaz gorecaz bakalim nasil oluyomus

# def hesaplamalar(x):
#     def kare_al(a):
#         return a ** 2
#
#     def karekok_al(a):
#         return a ** 0.5
#
#     def faktoriyel_al(a):
#         carpim = 1
#         for i in range (1,a+1):
#             carpim *= i
#         return carpim
#
#     kare = kare_al(x)                   #kare_al fonksiyonunu burada kare degiskenine atiyorum
#     karekok = karekok_al(x)             #ayni islemi karekok al icin de yapiyorum ve faktoriyel icin de. zaten return ile sonucu return ettigim icin sonuc da cikiyor.
#     fakt = faktoriyel_al(x)
#
#     return f"Karesi: {kare}   Karekoku:  {karekok}    Faktoriyeli: {fakt}"              #seklinde print edersek ekrana yazdiracaktir
#
# print(hesaplamalar(9))              #eger ustteki printi yapmadan boyle birakirsak cikti olarak bisey goremeyiz cunku fonksiyonlari tanimlamis olsak da fonksiyonlari cagirmadik.

#print(kare_al(6))           #seklinde bir ulasim saglayamayiz. ic ice fonksiyonda icteki fonksiyona dogrudan erisimimiz olamaz.!!!


#Simdi arglarla ilgili birseyler yapicaz birkac tane parametre alicak...

# def toplam_carpim(*args):               #args ile genel fonksiyon yani birden fazla deger alan dinamik fonksiyon tasarliyoruz.
#     def toplama(demet):
#         return sum(demet)                   #Buradaki return ifadeleri disariya deger donduremiyor, dis fonksiyona deger donduruyorlar...
#
#     def carpma(demet):
#         carpim = 1
#         for i in demet:
#             carpim *= i
#         return carpim
#     return f"Toplamlari: {toplama(args)}    Carpimlari: {carpma(args)}"         #burada da dis fonksiyon ile kendimize iletiyoruz.
#
#
# print(toplam_carpim(2,3,4,5,6))




# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\    Fonksiyonlardan Fonksiyon Döndürme islemini yapicaz simdi de       ////////////////////
#icerdeki fonksiyonu calistirmiycaz return ile geri dondurucez. return ile tamsayi liste geri donduruduk ama simdi de fonksiyon geri dondurucez

# def fonk(x):
#     return x*x
#
# # a = fonk(3)             #burada normal olarak sonuc atamasini yapiyoruz
# # print(a)                #print burada sonucu yazdiracaktir.
#
# b = fonk                #Burada ise fonksiyonun kendiisni bir degiskene atiyoruz, burada fonksiyonlarin da degiskene atanabildigini goruyoruz.
# print(b)                #hatta buarda b turunun bir fonksiyon oldugu ve bellekte tutuldugu yerin adres bilgilerini de gorebiliyoruz.
# print(b(5))             #burada ise b nin icne bir deger atayarak sonucu alabiliyoruz yani fonk(5) yerine b(5) yapabiliyoruz ve fonksiyona deger atiyoruz.




#simdi fonksiyon icinde fonksiyon olusturucaz ve onu icerde calistirmayacaz da geri dondurecez.

# def islem_sec(islem):
#     def toplama(*args):
#         toplam = 0
#         for arg in args:
#             toplam += arg
#         return toplam
#         #return sum(args)                #sum ile demetteki & array deki toplamlari alabiliyoruz ayni zamanda biz bu seger dongutyla yapmayi tercih ettik.
#
#     def carpma(*args):
#         carpim = 1
#         for arg in args:
#             carpim *= arg
#         return carpim
#
#     def ortalama(*args):
#         return sum(args) / len(args)
#
#
#     if islem == "toplama":
#         return toplama
#     elif islem == "carpma":
#         return carpma
#     elif islem == "ortalama":
#         return ortalama
#
# top_fonk = islem_sec("toplama")             #burada islem_sec fonksiyonuna "toplama" diye bir parametre gonderdik yani string olarak toplama dedik bunun degerine
# #print(top_fonk)                             #bunu boyle yazdirdigimiz zaman bunu bir fonksiyon oldugnu ve bellekte tutuldugu adresi gorebiliyoruz.
#
# print(top_fonk(2,3,4,5,6))              #bu sekilde deger verip islem yaptirinca sonuclari bastirir.
#
# carpma_fonk = islem_sec("carpma")
# print(carpma_fonk(2,3,4))
#
# ortalama_fonk = islem_sec("ortalama")           #ic ice fonksiyonlardan farkli olarak fonksiyonlkari icerde degil de disardida tanimlayip disarda calistiriyoruz,.
# print(ortalama_fonk(2,3,4,5,6))





#\\\\\\\\\\\\\\ Onemli olan kismi burassi ///////////
#simdi bir tane fonksiyon olucak kisi ismi secicez bir fonksiyon daha olucak onda da takim ismi secicez.

# def kisi_sec(kisi):
#     def takim_sec(takim):
#         return f"{kisi}, {takim}  takimini tutuyor."
#     #takim_sec()                #biz burada bunu boyle cagirirsak fonksiyonu calistirmis oluyoruz ama biz bunu istemiyoruz.
#     return  takim_sec               #biz bunu return etmek istiyoruz, disarida kullanicaz bunu.
#
# a = kisi_sec("Ali")         #burada a degiskenine kisi_sec fonksiyonuna attigimiz degeri ve fonksiyonun kendisini atiyoruz.
# b = kisi_sec("Veli")
#
# print(a("Newcastle United"))        #burada ise kisi parametresi otomatik olarak atandigi icin sadece a nin altinda takim isimlerini yaziyoruz cunku
# print(b("Adana Demirspor"))         # zaten f string icindeki kisi parametresi kisi sec fonksiyonundaki kisi parametresiyle ayni oldugu icin isim degerini oraya otomatik giriyor.





#\\\\\\\\\\\\\\ SIMDI SIRADA Fonksiyonlara Parametre Olarak Fonksiyon Göndermek KONUSU VARR //////////!!!!!!!!!!

# def topla(x,y):
#     return x + y
#
# def carpma(x,y):
#     return x * y
#
# def islem_yap(fonk,a,b):        #burada fonksiyon parametresini de alicak fonksiyonumuz
#     return fonk(a,b)            #burada ise olan sey bizim girdigmiz sayilari girdigimiz fonksiyona girip sonucu dondurmesi.
#
# print(islem_yap(topla,3,5))   #burada oneli olan nokta sudur topla yazdiktan sonra toplanin icine deger gondermiyoruz yani topla(3,5 ) demedik cunku o zaman topla fonksiyonuna
#                                     #degeri gonderip onu dondurecek biz burada son yaptigmiz fonksiyon olan islem_yap fonksiyonuna fonksiyon ismini ve degerleri gonderiyoruz.
#                                     #bu yaptigimiz dey bize islem_yap fonksiyonu icinde fonk parametresinde topla fonksiyonunu cagirmamizi sagliyor ve returndeki
#                                     #topla 3,5 islemini cagirip o fonksiyonun islemini yapmamizi sagliyor.
#
#                                     #isin ozu bir burada   def islem_yap(fonk,a,b):     fonksiyonundaki fonk a topla fonksiyonunu gonderdik ve 3 ve 5 i gonderdik.
#                                     #dolayisiyla bu bize topla fonksiyonunu dondurmus oldu.
# print(islem_yap(carpma,3,5))
#
#
# print(islem_yap(topla(3,5)))        #bu islemin sonucunda eger topla danb sonra () parantes icine degerleri yazarsak a ve b degerlerinin katip oldugnu bize soyleyecek..






#\\\\\\ Simdi guzel bir ornek yapalim bunula ilgili /////////////////

#aslinda yapacgimiz sey pyuthonda var o da map fonksiyonu ama simdi biz o fonksiyonu kendimiz yapacagiz, onu da ilerde isleyecegiz.


#burada yapacagimiz sey  gonderdigimiz listedeki elemanlarin karesini alip bununla yeni bir liste olusturmasi
# liste1 = [1,2,3,4,5]
# liste2 = [1,3,4,5,8,9,11]
#
# def kare_al(x):
#     return x*x
# def kup_al(x):
#     return x**3         #kupunu boyle aliyoruz.
#
# def map_fonk(fonk,liste):
#          sonuc = []               #yaapcagi sey su listedeki elemanlari tek tek elemanlari tek tek fonksiyona gonderecek gelen elemanlarla yueni bir liste olusturacak.
#          for i in liste:            #burada parametre olarak fonksiyona gonderilen listedeki butun elemanlari teke teker fonksiyona koyucak
#              sonuc.append(fonk(i))         #sonra oradan buldugumuz sonuclari da sonuc listesine ekliyoruz.
#          return sonuc                   #sonuc listesini geri donduruyoruz. yukarda bos olan sonuc listesini doldurduk.
#
# print(map_fonk(kare_al,liste1))         #gordugnuz gibi burada liste 1 deki butun elemanlarin karelerini alip liste sirasiyla yazirdik.
# print(map_fonk(kare_al,liste2))         #simdi de liste 2 dekilerin karelerini alip yazdirdik
#
# print(map_fonk(kup_al,liste1))          #bruada da fonksiyonu degistiriyoruz kup aldirtiyoruz liste 1 in
# print(map_fonk(kup_al,liste2))          #burada da liste 2 nin kupunu aliyoruz















