# \\\\\\\\\\\\\\\ Map Fonksiyonu /////////////////

#bizden parametre olarak bir tane fonksiyon ve liste aliyor, sonra listedeki elemanlari teker teker fonksiyona koyuyor ve elde edilen elemanlari tekrar liste haline getiriyor.
#yani: listedeki elemanlarin hepsi icin ayni islemi yapiyor. ornek:

# liste = [1,2,4,5,7]
# #listedeki elemanlarin hepsin fonksiyoan gondericez ve ordan gelen sonuclar ile yeni bir liste olusturucaz.
# def kare_al(x):
#     return x * x
# #eski yontemle boyle yapiyoruz yani map fonksiyonsuz haliyle hatirlayalim:
# liste2 = []  #bos biir liste olusuturyoruz.
# for i in liste:
#     liste2.append(kare_al(i))           #burasi da listenin icinde dolasan i leri kare al fonksiyonuna gonderip sonuclari liste2 ye yazdiracak.
#
# print(liste2)       #kareler burda
#
# #map ile yapalim
# liste3 = map(kare_al, liste)          #map fonksiyonunun icinde bizden 1 tane fonksiyon 1 tane de liste isteniyor.
#             #fonksiyonun kendisini gonderecegimiz icin () lari siliyoruz.
# #ilk basta direkt olarak liste seklinde bize vermez, biiz bunu nasil istiyorsak ona cevirip kullaniriz. demet istiyosak demet kume istiyorsak kume liste istiyorsak liste gibi.
# print(liste3)  #bu haliyle bunu bir map object oldugunu gosterir.
#
# liste3 = list(map(kare_al, liste))      #bu sekilde cevirmek istedigimiz ture cevirebiliyoruz sonrasinda kullanima hazir oluyor
# print(liste3)  #gorundugu gibi artik liste seklinde kullanima hazir.
#
# #kume icin:
# liste3 = set(map(kare_al, liste))
# print(f"Set version: {liste3}")
#
# #tuple icin
# liste3 = tuple(map(kare_al, liste))
# print(f"Tuple version: {liste3}")


#simdi lambda ile biseyler yapalim

# liste = [1,2,3,6,7,9]
# liste2 = list(map(lambda x : x*x, liste))
# #lambda da : dan onceki parametre : dan sonraki ise geri dondurecegi degerdi, yani burada hemen tek satirlik bir fonksiyon yaziyoruz. sonra mapin icine listeyi veriyorz.
# # lambda using     (     parametre     <- : ->     geri dondurulecek deger, kosul    )
# print(liste2)           #kareler alinmis vaziyette ciktimizi aldik.  artik tek satirda halledebiliyoruz.
#
#
# liste3 = list(map(lambda x : x ** 3,liste))
# print(liste3)   #burad da kuplerini aldik.





#simdi biraz daha ilerleyelim, 2 liste kullanalim.

#simdi yapmak istedigmiz sey elemanlarin ayni indexli olanlarinin toplamini donduren bir liste yapalim.
# liste1 = [1,3,4,7,8]
# liste2 = [3,5,9,0,1]
#
# def index_toplam(x,y):
#     return x + y
#
# sonuc = list(map(index_toplam, liste1, liste2))     #burada index_toplam'a x olarak liste1 i y olarak liste2 yi yolladik ve onlarin elemanlarini teker teker cekti ve topladi.
# print(sonuc)
#
#
# #Detay:  En az elemanli listemize gore islemleri yapar fonksiyonumuz. yani
#
# liste1 = [1,3,4,7,8]
# liste2 = [3,5,9,0,1]
# liste3 = [1,5,20]
#
# def index_toplam(x,y,z):
#     return x + y + z
#
# sonuc2 = list(map(index_toplam, liste1, liste2,liste3))
# print(sonuc2)           #hata vermez en az elemanliya gore map fonksiyonu durur.


# #simdi bunu lambda ile yapalim.
# liste1 = [1,3,4,7,8]
# liste2 = [3,5,9,0,1]
# liste3 = [1,5,20]
#
# sonuc3 = list(map(lambda x, y, z : x+y+z, liste1,liste2,liste3))
# print(sonuc3)





#simdi biraz farkli seyler yapalim

# urunler = [["Ayakkabi", 150], ["Pantolon", 120], ["Gomlek", 100], ["Ceket", 200]]
# #hepsine %10 indirm yapmak istiyoruz simdi.
#
# def indirim(x):
#     urun,fiyat = x[0],x[1]      #burada listemizin 0. elemanini yani urunu index[0] a yani stringe, fiyatini ise listemizin [1]. indexsine yani fiyata esitledik.
#     fiyat = fiyat * (9/10)      #burada da fiaytmizi guncelledik %10 indirim yaptirdik.
#     return [urun,fiyat]         #burada ise yukarda esitledigimiz urunleri ve fiyatlari dondurttuk.
#
# sonuc = list(map(indirim,urunler))      #fonksiyonumuzu cagirdik ve listemizi cagirdik, fonksiyon zaten listemizin icine girip gerekli islemleri yapti.
# print(sonuc)





# #baska bir sey daha yapalim
#
# isimler = ["AhMet", "aYse", "oNur", "KaAn"]
# #hepsini buyuk veya kucuk harfe cevirmek istiyoruz.
# isimler2 = list(map(lambda x : x.lower(),isimler))     #lower hepsini kucuk yapmaya yariyordu
# print(isimler2)  #tum isimler ayni oldu hepsi kucuk harfle yazildi.
#
#
# #simdi lower fonksiyonunda () lari kullandik neden fark nedir yukarda cunku () lari yazmadik. fark su: biz kendi koyduklarimizda fonksiyonu parametre olarak gonderdik
# #biz simdi kendi yazdigimiz fonksiyonlarda () lari koyarsak sonucunu parametre olarak gondermis olacaktik.

























