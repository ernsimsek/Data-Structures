stack = []      #! stack e her eleman eklediğimizde en üste ekleniyor, her eleman çıkarmak istediğimizde ise en üstten çıkıyor
                #! yani son giren ilk çıkıyor

stack.append("a")    #! append stack e eleman ekler

stack.pop()          #! pop stack den eleman çıkarır

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
stack.append("e")   #? her eleman en sona ekleniyor
print(stack)

stack.pop()
stack.pop()
print(stack)        #? kaldırdığımız her eleman da listenin sonundan kalkıyor

print(stack[-1])    #? listenin en üstendeki elemanı verir

print(not stack)    #? stack in boş olup olmadığını dönüyor (boşsa true doluysa false)

print(len(stack))   #? listenin boyutunu döner

                #! liste stack olarak kullanıldığında boyutu büyüdükçe hız sorunları ortaya çıkıyor.
                    #? liste onu tutan bellek bloğundan daha fazla büyürse bellek tahsisi yapılması gerekiyor 
                    #? buda append çağrılarının diğerlerinden çok daha uzun sürmesine neden oluyor

                #todo bu yüzden queue nun LifoQueue modelini kullabiliriz.

from queue import LifoQueue     #? bu sayede listenin sorunlarına takılmadan stack veri yapısını kullanabiliyoruz

stack3 = LifoQueue(maxsize=3)

stack3.put("a")             #? put eleman ekliyor 
stack3.put("b")
stack3.put("c")

stack3.get()                #? get eleman kaldırıyor
stack3.get()

print(stack3.get())         #! yalnızca get ile eleman kaldırarak elemanları görebiliyoruz
