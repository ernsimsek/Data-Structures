class Node:                                #* kendi verisini ve sonraki düğümün referansını tutması için Node sınıfı oluşturduk.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:                       #* Bağlı listeyi yönetecek bir LinkedList sınıfı tanımladık. 
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):      #* insertAtBegin fonk.sunu ile bağlı listenin başına yeni bir düğüm ekliyoruz.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Node with data '{data}' added at the beginning.")

    def insetAtIndex(self, data, index):       #* Belirli bir index e düğüm ekler.
        if index == 0:
            self.insertAtBegin(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            print(f"Node with data '{data}' added at index {index}")
        else:
            print("Index not present. Insertion failed.")

    def insertAtEnd(self, data):                #* Listenin sonuna düğüm ekler.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Node with data '{data}' added as the first node")
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        print(f"Node with data '{data}' added at the end.")

    def updateNode(self, val, index):           #* Belirtilen bir index'teki düğümün verisini günceller.
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.data = val
            print(f"Node at index {index} updated to '{val}'.")
        else:
            print("Index not present. Update failed.")

    def remove_at_index(self, index):           #* Belirli bir index'teki düğümü siler.
        if self.head is None:   #! Bunun için önceki düğüm referansını silinecek düğümden sonraki düğümün referansı olarak tanımladık.
            print("The list is empty. Nothing to remove.")
            return
        if index == 0:
            self.remove_first_node()
            return
        current_node = self.head      
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None and current_node.next is not None:
            print(f"Node at index {index} with data '{current_node.next.data}' removed.")
            current_node.next = current_node.next.next
        else:
            print("Index not present. Removal failed.")

    def remove_first_node(self):                #* Bağlı listenin ilk düğümünü siler.   
        if self.head is None:
            print("The list is empty. Nothing to remove.")
            return
        print(f"First node with data '{self.head.data}' removed.")
        self.head = self.head.next

    def remove_last_node(self):                 #* Bağlı listenin son düğümünü siler.   
        if self.head is None:
            print("The list is empty. Nothing to remove.")
            return
        if self.head.next is None:
            print(f"Last node with data '{self.head.data}' removed.")
            self.head = None
            return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        print(f"Last node with data '{current_node.next.data}' removed.")
        current_node.next = None

    def sizeOfLL(self):                         #* Bağlı listedeki düğüm sayısını verir.
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(result) if result else "Empty List"
    



