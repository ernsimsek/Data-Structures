
#! Liste birbirine bağlı düğümlerden oluşuyor

# [ a | ref(b) ]    #* [a] ---> head : ilk düğüm
# [ b | ref(c) ]
# [ c | ref(d) ]
# [ d | none ]


from linked_list import LinkedList  

llist = LinkedList()        #? oluşturulan tüm fonksiyonlar kullanılabilir. 
print(llist)

llist.insertAtBegin(5)      #? listenin başına eleman ekledi
llist.insertAtBegin(6)
llist.insertAtBegin(7)
print(llist)

llist.insetAtIndex(3, 1)    #? listede belirli bir konuma eleman ekledi
print(llist)

llist.insertAtEnd(8)        #? listenin sonuna eleman ekldi
print(llist)

llist.updateNode(10, 0)     #? istediğimiz düğümün verisini güncelledi
print(llist)

llist.remove_at_index(0)    #? listedinin belirli bir konumdaki elemanını kaldırdı
print(llist)

llist.remove_first_node()     #? listenin ilk elemanını kaldırdı
print(llist)

llist.remove_last_node()
print(llist)

print(llist.sizeOfLL())     #? bağlı listenin uzunluğunu verir