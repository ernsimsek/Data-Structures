
#*---------------------------------------------------------
#!                                                          ---> kök (root) (Ağacın en üstündeki düğüm)
#*                         (1)                              
#*                   ref(2) | ref(3) 
#*
#*---------------------------------------------------------
#!                                                          ---> ebeveyn (parent)       Yükseklik = 3 (en uzun dalın birimi)
#*            (2)                      (3)                  
#*      ref(4) | null            ref(5) | null
#*
#*---------------------------------------------------------
#!                                                          ---> çocuk (child)
#*      (4)                                   (5)           
#*  null | null                           null | null
#?                                                               yaprak (leaves) (hiç bir çocuğu olmayan düğümler)
#*---------------------------------------------------------


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourthNode = Node(4)

firstNode.left = secondNode
firstNode.right = thirdNode             #?   binary tree oluştu.
secondNode.left = fourthNode


