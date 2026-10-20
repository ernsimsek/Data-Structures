
#todo FIFO : first in first out ---> Listeye ilk giren ilk çıkar

#? Eleman eklemek veya çıkarmak ---> O(1)

from collections import deque       #? Kuyruk oluşturmak için collections'ın deque modulünü kullandık

q = deque()

queue = deque(["ali", "ali", 1, 2.5, True])  #? string, integer, double, boolean gibi istediğimiz her değişkeni ekleyebiliyoruz

queue.append(3)                     #? append eleman ekler
print(queue)

queue.pop()                         #? pop eleman kaldırır
print(queue)

print(not queue)                    #? not eleman kontrolü

print(queue.count("ali"))           #? count elemanın kaç kez tekrar ettiğini sorgular

print(len(queue))                   #? len queue'nun uzunluğunu verir

