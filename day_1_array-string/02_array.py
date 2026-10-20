
tam_sayi = [1,2,3]
string_listesi = ["ali","eren"]
sayi_string = ["ali", 1, 2]

veriler = (1, "ali", 2)
veriler_listesi = list(veriler)
print(veriler_listesi)

sifir_tablosu = [0] * 5
print(sifir_tablosu) 

liste = []
liste.append(10)    #! Girilen değer listenin sonuna ekleniyor.
print(liste)

liste.insert(0, 5)  #! Spesifik bir konuma (0. index e 5 değeri) değer eklemek için kullanılır.
print(liste)

liste.extend([3, 10, 25])   #! Birden fazla eleman eklemek için kullanılır, listenin sonuna ekler.
print(liste)  

liste[0] = 1    #! Elemanların değer değişimi işlemi.
print(liste)

# liste.remove(1)   #! Kaldırmak istediğimiz elemanı parametre olarak yazıyoruz.
# print(liste)

# liste.pop(-1)   #! Değişken değeri ile değilde index numarası ile kaldırmak istersekte pop metodunu kullanıyoruz.
# print(liste)

# del liste[1]    #! del ile silmek istediğimiz elemanın index numarasını yazıp siliyoruz.
# print(liste)

for item in liste:  #! For döngüsü ile listenin elemanlarını dolaşabiliyoruz. Her döngü listenin elemanlarını temsil ediyor.
    print(item)