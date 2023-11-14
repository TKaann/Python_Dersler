# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ Iterators Kullanimi ve Ornekleri ///////////////////////////////////

#iterator, iterable ve iteration kavramlarina bakicaz.
#__iter__() ve __next__() kavramlari.


# sayilar = [1,2,3]
#
# for sayi in sayilar:
#     print(sayi)

#burada olan sey sayi once 1 oluyor ekrana yazdiriliyor ardindan 2 ve 3 olup ekrana yazdiriliyor, simdi gelelim iteration kavramina:
#iratation kavrami zatn anlam olarak da adimlama anlamina geliyor. bir nesnenin elemanlarini teker teker ziyaret etme islemine iteration deniyor.

#iterable ise uzerinde adimlama yapilan demek, yani burdaki sayilar listesi uzerinde adimlama yapilabilecegi icin bir iterabledir,
#sadece listeler degil dongulerde kullanabilecegiimiz butun nesneler iiterabledir.

#simdii gelelm iterator kavramina, iterator kavrami en onemlisidir.
#islev ise basettiigiimiz adimilama isiini yapan nesnedir. ve soyle bir is yapar:
#butun elemanlar teker teker geziyor ancak nerde kaldigini da unutmuyor. eleman kalmayinca da sonlandriyor.






#simdi biz sayilar = [1,2,3] bu listeye iterable dedik, peki tipini bilmedigmiz bir seyin iterabgle olup olmadigini da soyle ogrenicez.

# sayilar = [1,2,3]
# print(dir(sayilar))   #bu dir bize sayilar nesnesi ile kullanabilecegimiz metodlari gosterir.
# eger bir nesnenin metodlari arasinda '__iter__' varda o nesnenin iterable oldugunu gosterir.   eger iterse dongulerle kullanilabilir anlamina gelir.





#peki bu __iter__() ne yapar. bu iter bize bir iterator dondurur. simdi bakalim kullanimina

# sayilar = [1,2,3]

# i_sayilar = sayilar.__iter__()
# i_sayilar1 = iter(sayilar)   #iki kullanim da aynidir, ikisi arasinda fark yok. bu kullanim daha sadedir.

# print(type(i_sayilar))    #liste oldugu icin list iterator geldi,




#simdi iteratoru iterator yapan sey ise budur!!:

# sayilar = [1,2,3]
#
# i_sayilar1 = iter(sayilar)

# print(dir(i_sayilar1))      # '__next__' metodu, bir iterator u iterator yapan next metodudur.
# next metodu ise bir sonraki elemana nasil gececegini soyleyen metottur. yani next metodu cagirildiginda iterator bir sonraki elemana geciyor diyebiliriz.



#simdi bunu gosterelim.


# sayilar = [1,2,3]
#
# i_sayilar = iter(sayilar)          #simdi burada sayilar listesini iteratora cevirip i_sayilar' a atadik. simdi next metodunu kullanalim.
#
# print(next(i_sayilar))          #1 yazdirdi
# print(next(i_sayilar))          #2 yazdirdi
# print(next(i_sayilar))          #3 yazdirdi    her calistirdigimizda nerden kaldiysa ordan devam ediyor, iste bu bir iteratoru iterator yapan seydir.







#burada bir dongunun nasil calistigini az cok anlattik simdi dongunun nasil calsitigni daha derin gorelim:

#dongu calistirildigi zaman ilk once nesnenin iter metodunun cagiriyor ve bize bir iterator donduruyor, simdi hata alana kadar yani:
# eleman kalmayana kadar iteratora next metodunu uyguliycaz hata geldiginde ise donguden cikicaz. simdi bunu manuel olarak yapalim

# sayilar = [1,2,3]
#
# i_sayilar = iter(sayilar)
#
# while True:
#     try:        #yapacagimiz islemleri buranin icine yaziyoruz.
#         sayi = next(i_sayilar)
#         print(sayi)
#     except StopIteration:   #hata alirsak burda yakaliyoruz. burda ne hatasi aliyoruz listemizdeki elemanlarimiz bittigi zaman stopIteration hatasi aliyoruz.
#         break

#simdi bir dongude olan seyleri tamamen gordun, dongude olan sey aslinda bu. bi iter olustur sonra next next de hata aldiginda cikis yap.
#bu kod blogunu calistirdigimiz zaman bize dongudeki ciktinin aynisini veriyor.







#simdi farkli ornekler yapalim
#bir class olusturalim ve olusturdugumuz classin iteratorunu olusturalim

#range fonksiyonuna benzer bir class olusturalim

# class new_range:
#     def __init__(self,start,end):
#         self.yazilacak = start          #start ile end arasindaki butun saylari yazdiracagim icin yazilacak dedim.
#         self.end = end
#     def __iter__(self):            #simdi bunu iterable yapalim
#         return self         #iterable olarak dondurduk simdi bir dongu olmasi icin next metodu olmasi lazim,. simdi onu uretelim.
#
#     def __next__(self):  #next metodunu urettik.
#         if self.yazilacak >= self.end:           #burada ise sunu kontrol ediyortuz: yazilacak sayi sinira geldi mi gelmedi mi. hata firlatacak yer bruasi.
#             raise StopIteration                 #eger sonuna gelmisse Stopiteration hatasini firlatiyoruz.
#
#         deger = self.yazilacak      #simdi bu blokta yaptigimiz sey ise yazilacak degerini bir degiskene atayip onu return ettirmmek, yani oncesinde
#         self.yazilacak += 1         #degerimizi yazdiriyoruz sonrasinda artiriyoruz ama atammasini sonraki adimda yapiyoruz, return ettigimiz seye artirmma yapamadigimimz icn.
#         return deger
#
# #simdi bunu calistiralim.
#
# sayilar = new_range(10,30)
# for i in sayilar:
#     print(i)            #gordugunuz gibi ayni range fonksiyonu gibi belirledigimiz 2 sayi arasinda degerleri dondurdu.






































