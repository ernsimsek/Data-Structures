s = {"bu", "bir", "settir"}

list_to_set = set(["bu", "bir", "listeydi", "ama", "sete", "dönüştü"])
print(list_to_set)

a = {"ali", "ali", "ali", "ali"}        #! set de aynı elemanlardan birden fazla kez bulunmuyor 
print(a)                                #? bu yüzden çıktı sadece "ali"

karisik = {"ali", 5, 3.14, True}        #! bir sette string, integer, double, boolean vs istediğimiz her değeri saklayabiliyoruz.
print(karisik)

fs = frozenset(["bu", "dondurulmuş", "bir", "settir"])     #! frozenset e sonradan hiçbir değer eklenemez
# fs.add("eklenemez")

veriler = {"a", "b", "c", "d"}

set1 = {"ali", 1}
set1.add("eren")
print(set1)

sayilar = {1, 2, 3, 4}
harfler = {"a", "b", "c", "d"}
sayilar_ve_harfler = sayilar.union(harfler)      #! union iki veri setini (kümesini) birleştirir.
print(sayilar_ve_harfler)

asal_rakamlar = {2, 3, 5, 7}
cift_rakamlar = {2, 4, 6, 8}
ortaklar = asal_rakamlar.intersection(cift_rakamlar)      #! intersection veri setlerindeki ortam elemanları bulur (kesişim kümesi)
print(ortaklar)

fark = cift_rakamlar.difference(asal_rakamlar)     #! difference iki set arasındaki farkı bulur
print(fark) 

fark.clear()        #! clear set i temizler
print(fark) 

print(2 in asal_rakamlar)
print(4 not in asal_rakamlar)
print(asal_rakamlar == cift_rakamlar)
print(asal_rakamlar < cift_rakamlar)

for i in asal_rakamlar:
    print(i)


