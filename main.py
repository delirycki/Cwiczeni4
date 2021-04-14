# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#zad1

# lista=[]
# for f in range(1,31):
#     lista.append(f)
# #print(lista)
#
# p = open("zad.txt","w")
#
# for g in lista:
#     p.write(str(lista[g-1]*2)+"\n")
#
# p.close()

#zad2
#
# with open("zad.txt", "r") as plik:
#     for linia in plik:
#         print(linia,end="")

#zad 3
#
# plik = open("zad.txt","w")
#
# for i in range(5):
#     zdanie = input("Napisz jakieś zdanie : ")
#     plik.write(zdanie +"\n")
#
# plik.close()
#
# with open("zad.txt","r") as plik:
#     for linia in plik:
#         print(linia,end="")

#Zadanie 4

# class NaZakupy():
#     def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswielt_produkt(self):
#         print("Kupiles "+self.nazwa_produktu+" w ilości "+self.ilosc+self.jednostka_miary+" za "+ self.cena_jed)
#     def ile_produktu(self):
#         print("Kupiłeś "+self.ilosc+self.jednostka_miary)
#     def ile_kosztuje(self):
#         print(int(self.ilosc)*int(self.cena_jed))
#
# q = NaZakupy("Mąka","3","kg","4")
# q.wyswielt_produkt()
# q.ile_produktu()
# q.ile_kosztuje()


#Zadanie 5

# class Ciagi():
#     def __init__(self):
#         self.a1 = None
#         self.r = None
#         self.n = None
#         self.ciag = []
#
#     def wyswiel_dane(self):
#         for elementy in self.ciag:
#             print(elementy)
#     def pobierz_parametry(self,a1,r,n):
#         element = a1
#         for i in range(1,n+1):
#             self.ciag.append(element)
#             element=element +r
#     def policz_sume(self,a1,r,n):
#         print(((2*a1+(n-1)*r)/2)*n)
#
# p = Ciagi()
# p.pobierz_parametry(1,3,4)
# p.policz_sume(1,3,4)
# p.wyswiel_dane()

# #Zad6
# class Robaczek:
#     def __init__(self,x=0,y=0,krok=1):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self,ile_krokow):
#         self.x=self.x + (self.krok * ile_krokow)
#     def idz_w_dol(self,ile_krokow):
#         self.x= self.x - (self.krok * ile_krokow)
#     def idz_w_lewo(self,ile_krokow):
#         self.y=self.y-(self.krok * ile_krokow)
#     def idz_w_prawo(self,ile_krokiw):
#         self.y=self.y + (self.krok * ile_krokiw)
#     def pokaz_gdize_jestes(self):
#         print("Jestem "+ str(self.x) +" "+ str(self.y))
#
#
# r=Robaczek()
# r.idz_w_gore(10)
# r.idz_w_dol(10)
# r.idz_w_lewo(10)
# r.pokaz_gdize_jestes()








