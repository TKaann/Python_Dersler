# \\\\\\\\\\\\\\\ Generators Kullanimi //////////////////

#generatorler verileri sirasiyla ve sadece gerektiginde ureten nesnelerdir. generatorler bellek kullanimini onemli olcude azaltarak daha verimli kodlar yazmamiza yardimci olur
#buyuk veri kumeleriyle calisirken tum verilerin bellekte saklanmasi yerine sadece ihtiyac duyulan itemlerin elemanlarin uretilmesi sayesinde bellek kullanimi optimize edilir.
#ozellikle buyuk dosyalarda calisirken bu ozeligin onemi buyuktur. generatorler sayesinde veri ogeleri sadece gerektiginde uretilir bu duruma yazilim dilinde ise:
#lazy evolution derler. bu yalnizla gerekli ogelewrin islenmesiyle zaman ve kaynak kullaniiiminiin optimize edilmesiine yardimci olur.
#kodun daha hizli calismasiiina ve daha verimlii olmasina katki saglar. generatorler kodun daha okunabiliir ve sade hale gelmesine yardiimc olurlar.

#dosyalari satir satir okurkern ya da ag uzerinde veri alip gonderirken generatorler kullanilabilir. dosyanin tum icerigini bellege yuklemek yerine generatorler sayesinde
#dosyanin sadece bir kismin isleyerek bellek kullanimini azaltiriz. ayrica ag uzerinde buyuk veri aktarimlarinda da generatorler sayesinde veriler parcalar halinde
#islenebilir ve boylece verimililiik artir.

#generatorleri anlamamiz icin once yield denilen anahtar kelimeyi anlamamiz gereklidir.
#yield pythonda anahtar kelimedir ve generator fonksiyonlar olusturduugmuzda deger dondurmek icin kulanilir. returne benzer ama fonksiyonun duraklatilmasina ve bir sonrkai
#cagrida kaldigi yerden devam etmesine olanak tanir bu sayede generator fonksiyonlari bellek dostlari ve daha vermli calisir. yield sayesinde generator fonkisoynlari
#bellek dostu olur ve daha verimli olur.

#simdi orneklerimize gecelim..:


#yine range gibi bir fonksiyon olusturuyoruz.
# def number_generator(limit):
#     number = 0
#     while number < limit:
#         yield number            #burada sanki return number yapiyor gibiyiz ama number generatoru cagiran nersiyle oraya return eder ama program bitmez devam eder.
#         number += 1
# # generator_func = number_generator(3)
# #
# # print(next(generator_func))
# # print(next(generator_func))
# # print(next(generator_func))
#
# #ustteki ornekte bir uygulamasini gosterdik ama tabiki de normalde boyle kullanmiyoruz. normalde dongulerle kullaniminu yapiyoruz.
#
# #dongu kullanimi ise boyledir:
#
# for n in number_generator(3):
#     print(n)

#gordugunuz gibi dongulerle kullanimi cok daha rahat oluyor. Stopiteration u gorene kadar devam ediyor gordukten sonra ise birakiyor.




#simdi cift sayilari hesaplayan bir generator fonksiyon yapalim

# def even_number(limit):         #limit yaziyoruz cunku generatorlerin kac defa donecegini bilmemiz gerekiyorki for dongulerini kullanabilelim yoksa sonsuz kere donerler.
#     number = 0
#     while number < limit:
#         if number % 2 == 0:
#             yield number
#
#         number += 1
#
# for n in even_number(100):
#     print(n, end=" ")            #100 e kadar butun cift sayilari aldik.
#     #end = " "    ile yan yana yazdirdik.





#simdi fibonacci yazan generator yapalim

# def fibo_generator(lenght):
#     a, b = 0, 1
#     count = 0
#     while count < lenght:
#         yield a
#                                 # temp = a            #gecici bir deger verdik burada
#                                 # a = b
#                                 # b = temp + b        #bu kullanim yerine altindaki de trercih edilebilir, daha kisa olur.
#         a, b = b, a + b
#         count += 1
#
# for fib in fibo_generator(10):
#     print(fib, end=" ")



#random sayi uretelim
# import random
#
#
# def even_random_generator(limit, low, high):
#     count = 0
#     while count < limit:
#         random_number = random.randint(low,high)
#         if random_number % 2 == 0:
#             yield random_number
#         else:
#             continue
#         count += 1
#
# for number in even_random_generator(30,1,999):
#     print(number, end=" ")



#verdigimiz listelerin elemanlari karistira karistira donduren bir generate fonksiyon yapalim
# import random
#
# def shuffled_list(*args):
#     combined_list = []
#     for arg in args:
#         combined_list += arg
#
#
#     random.shuffle(combined_list)
#
#
#     for element in combined_list:           #neden while kullanmadik cunku zaten bu bir liste oldugu icin sonu var sonu oldugu icin de for kullandik
#         yield element
#
# list1 = [123,345645,2342345457,23453,456,13]
# list2 = [4676,34556568,56742,4,678,3,325,773,1]
# list3 = [2345,2345,4562,3]
#
# for number in shuffled_list(list1,list2,list3):
#     print(number, end=" ")





#Son ornegimiz network isi yapilirken nasil kullanacagimiz

# import requests
# #simdi yapmak istedigimiz sey internetten bir yere girip cok buyuk veri cektigimizde bunu bize parca parca versin
#
#
# def download_line(url, max_line):
#     response = requests.get(url, stream=True)       #burasi bir urlden gidip veri cekiyor.
#     response.raise_for_status()             #eger cekemezse bir hata varsa 404 gibi 505 gibi burda hata firlatiyor
#
#
#     line_count = 0                      #kac satir okudugmuzu sayiyoruz.
#     for line in response.iter_lines(decode_unicode=True):           #response un icindeki degerleri teker teker oku diyoruz. requestin icinde boyle bir sey var faydalaniyoruz
#         if line_count >= max_line:
#             break                   #10 satir okunduktan sonra donguyu kiriyoruz
#         yield line                      #10 satirdan az okunmussa onu yield ediyoruz.
#         line_count += 1
#
#
# my_url = "https://twitter.com/AltayCemMeric"
# max_line_to_download = 10
#
# for url_line in download_line(my_url,max_line_to_download):
#     print("[Line]", url_line)                       #ve burada dondurup print ediyporuz










#iteratorsun benzeridir, mantik aynidir.

# def uretec():
#     sayi = 0
#     print(sayi, ". adim")
#     yield sayi          #yield ozel bir dondurme yontemidir return yerine kullanilir ve birden fazla kullanilir.
#
#     sayi += 1
#     print(sayi, ". adim")
#     yield sayi
#
#     sayi += 1
#     print(sayi, ". adim")
#     yield sayi
#
# #returnde oldugu gibi tek seferde geri dondurmeyecek adim adim geri dondurecek.
#
# # a = uretec()
# #
# # next(a)         #sayinin ilk adimini cagiriyoruz.
# # next(a)
# # next(a)
#
# #simdi bunlari normal sekilde cagirdik ve print ettirdik, simdi dongu icinde cagiralim.
#
#
# b = uretec()
#
# for x in b:
#     print(x)

















































