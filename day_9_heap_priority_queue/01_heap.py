
#!  En çok kuyruk uygulamalarında kullanılıyor çünkü kök de en küçük veya en büyük eleman bulunuyor

import heapq                #* heapq modulünü kullanarak heap oluşturduk

li = [5, 7, 9, 2, 3]        #* verilerle bir liste oluşturduk

heapq.heapify(li)           #! heapify metodu ile listeyi heap'e dönüştürdük. Bu dönüşüm işlemi bir, ikili ağaç üzerinden oluyor.

print(li)                   #* kök de en küçük bulunuyor

neg_li = [-x for x in li]       #? listedeki değerlerin negatif hali ile heap i oluşturup tekrar pozitife çevirdik
heapq.heapify(neg_li)
max_heap = [-x for x in neg_li]     #? bu işlem kök de en büyüğün yer almasını sağladı

print(max_heap)

heapq.heappush(li, 4)           #* heappush eleman ekler
print(li)

heapq.heappop(li)               #* heappop kök elemanı kaldırır
print(li)

heapq.heappushpop(li, 10)       #* heappushpop hem bir eleman ekler hemde kök elemanı kaldırır
print(li)

print(heapq.nlargest(2, li))       #* nlargest en büyük belirli sayıdaki elemanları bulur (burada en büyük iki sayı 10 ve 9)

print(heapq.nsmallest(2, li))      #* nsmallest en küçük belirli sayıdaki elemanları bulur (burada en küçük iki sayı 4 ve 5)

for _ in range(len(li)):            #* Bir heap in verilerini sıralamak için her defasında kök düğümü heap'den kaldırıp yazdırıyoruz.
    print(heapq.heappop(li))

