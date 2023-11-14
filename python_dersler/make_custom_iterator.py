# \\\\\\\\\\\\\\\\\\ Custom Iterator Olusturma /////////////////

# cumle = "Lokomotif Klavye Osmanli Soylusu Ayi Rap"
#
# for i in cumle:
#     print(i)            #simdi burada print islemi yaptigmizda alt alta yuaziyor biz kelime kelime olarak yazmasini istiyoruz diyelim buna gore bi iterator tasarlayalim


# class cumle:
#     def __init__(self,cumle):
#         self.cumle = cumle
#         self.index = 0
#         self.kelimeler = self.cumle.split()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.kelimeler):
#             raise StopIteration
#         dondurulecek = self.index
#         self.index += 1
#         return self.kelimeler[dondurulecek]
#
#
# yeni_cumle = cumle("Lokomotif Klavye Osmanli Soylusu Ayi Rap")
# for kelime in yeni_cumle:
#     print(kelime)









































