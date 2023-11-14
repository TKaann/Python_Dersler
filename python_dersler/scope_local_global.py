# \\\\\\\\\\\\\\\\ Değişkenlerin Kapsama Alanları (Scope) | Local, Global Değişkenler /////////////////////////

#local , enclosing, global, built-in variables.


# x = "global x"
#bu bir global degiskendir peki neden cunku programimin en disinda tanimlandi, buranin altinda acacagimi butun scopelarda bu taninacaktir, scope ise {} dur yani:
#{} isaretinin icine girdigmizde bir tab iceri giriyoruz, iceri girdigimizde {} icindeki bu 2 {} arasindaki her tab girinti bastan sona scope oluyor. ornek olarak:
# for i in range(10):
#     {
#         print(i)
#     }
#normalde biz pythonlar buralarda {} isareteleri kullanmayiz ama bu normalde vardir ve bunlara scope deriz.
#bu scopelarin icinde olusturdugum degisken ise local degiskendir. scope un disinda kullanilamaz ama altinda bir scope daha olursa kullanilabilir. ornek olarak:
# for i in range(10):
#     {
#         print(i)
#         d = "Merhaba"
#     }
#print(d)           #bunu yapamayiz cunku d yi icerde tanimladik

# for i in range(10):
#     {
#         print(i)
#         d = "Merhaba"
#         while True
#         {
#               print(d)                #bunu yapabiliriz cunku d degiskenimiz kendisinden daha disardaki bir scope da tanimlandi.
#         }
#     }

#Lokal ve global degisken mantigimiz temel olarak bu sekildedir.


#simdi fonksiyonlardan ornek verelim.:

# x = "global x"
#
# def fonk():
#     x = "lokal x"
#     print(x)
#
#
# fonk()          #burda lokal x yazdi
# print(x)          #burda global x yazdi sebebi ise soyle, fonksiyon icine disardan mudahil olamayiz. fonksiyon icindeki degiskene sadece fonksiyonun icinden erisebiliriz


# x = "global x"
#
# def fonk():         #eger fonksiyondan x i silip yazdirirsak
#     print(x)
#
# fonk()
# print(x)
#ikisinde de global x yazacaktir, bunun sebebi ise en ustte bahsettigim gibi x in globalde tanimlanmis olup her yerden erisilebilir oldugundandir.



#simdi enclosingi aciklayalim:

# x = "global x"
#
# def outer():            #outer demek disardaki anlamina geliyor yani global degil bu.
#     x = "enclosing x"
#     print(x)
#
#     def inner():
#         x = "lokal x"
#         print(x)
#     inner()
#
# outer()
# print(x)

#buradaki x leri teker teker yorum satirlarina alip denemeler yapabilirsiniz mantigi kavramak icin.






#simdi baska bir ornek verelim

# x = "global x"
#
# def fonk():
#     x = 5
#
# fonk()
# print(x)

#simdi normal sartlarda bu durumda fonksiyon icindeki x globaldeki x e muhdahale edemiyor yani onu degistiremiyor, ama onu degistirmek istersek global keywordunu kullaniriz.
#ornek vermek gerekirse:


# x = "global x"
#
# def fonk():
#     global x
#     x = 5
#
# fonk()
# print(x)        #bruada gordugumuz gibi x artik fonksiyonun icinde degistirdigimiz degeri aldi artik x imiz 5 oldu. globale mudahale ettik global keywordu ile.







#simdi bunu fonksiyonlar icinde yapalim.

# def outer():
#     x = "encoding x"
#     print(x)            #bruada normal sekilde encoding x imizi yazdieriyoruz,
#     def inner():
#         nonlocal x
#         x = 5
#     inner()
#     print(x)            #bruada da normalde encoding x yazmasi gerekyior ama biz ondan onceki x i nonlocal ile onceki fonksiyon icinden degistirdigimiz icin artik 5 yazdirdik.
#
# outer()



#built in ise  sum max lambda  gibi ozel keywordleri kullanamayiz. buna dikkat edelim bunlar anahtar kelimelerdir.





























