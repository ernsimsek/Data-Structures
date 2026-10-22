
#* Bir listedeki her eleman için kendinden sonraki en büyük elemanı bulan bir algoritma düşünelim.
# 
#? Kaba kuvvetle çözmeye çalıştığımız da her bir eleman için listenin tamamını tekrardan dolaşmak zorundayız
#! Brute force = n^2
#todo Bunun yerine listeyi tersten dolaşıyoruz. Bir artan stack kullanarak sadece daha büyük elemanla hesaplıyoruz. Eğer stack boş olursa bu eleman için daha büyük eleman olmuyor. Her kontrolden sonra elemanı artan yapıdasındaki stack'e ekliyoruz. Eğer stack boş olmazsa da stack'in tepesinde ki eleman şuanki elemandan sonraki daha büyük eleman oluyor. Sonraki elemanları da artan stack yapısına uygun şekilde stack'e ekliyoruz ve sonuca ulaşıyoruz. Böylece listeyi tek bir kez dolaşıyoruz. Bu algoritma çok daha hızlı çalışıyor.
#! Monotonic stack = n

#* Monotonic stack sonraki en büyük veya en küçük sayıyı bulma (yukarıdaki algoritma), aralık hesaplama ve sıralama kısıtlamarıyla ilgili problemleri çözmede kullanılıyor.


#? Artan monotonic stack
def monotonicIncreasing(nums):
    stack = []                          #? boş bir stack tanımlandı

    for num in nums:                    #? listeyi dolaşıyoruz
        while stack and stack[-1] > num:    #* stack'n dolu olduğu ve stack'teki son elemanın şuan ki elemandan büyük olduğu sürece çalışacak bir while döngüsü tanımladık
            stack.pop()                     #* koşul sağlandığı sürece stack'teki son elemanı kaldırıyoruz.
        stack.append(num)               #? elemanlar kaldırıldıktan sonra stack'e şuan ki elemanı ekliyoruz.
                                    #* Böylece şuan ki eleman stack'de kendinden büyük olan elemanları kaldırdıktan sonra stack'e ekleniyor.
    return stack                    #? son olarak stack'i return ediyoruz. artan monotonic stack tamamlandı.

nums = [3, 1, 4, 1, 5, 9, 2, 6]         #? bir liste üzerinde test ediyoruz.
result = monotonicIncreasing(nums)
print("Monotonic increasing stack: ", result)       #* ----> [1, 1, 2, 6]

#? Azalan monotonic stack
def monotonicDecreasing(nums):
    stack = []

    for num in nums:
        while stack and stack[-1] < num:     #? sadece büyük koşulunu küçük ile değiştiriyoruz.
            stack.pop()
        stack.append(num)

    return stack

result = monotonicDecreasing(nums)
print("Monotonic increasing stack: ", result)