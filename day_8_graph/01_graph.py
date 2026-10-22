V = 4
mat = [[0] * V for _ in range(V)]

def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

add_edge(mat, 0, 1)         #? graph verilerini matriste iki boyutlu şekilde sakladık
add_edge(mat, 0, 2)         #? bağlantı olursa 1 olmazsa 0
add_edge(mat, 1, 2)
add_edge(mat, 2, 3)

for row in mat:
    print(" ".join(map(str, row)))

adj = [[] for _ in range(V)]

def added_edge_list(adj, i, j):         #? bağlı liste kullanmak bellekte daha az yer kaplar
    adj[i].append(j)
    adj[j].append(i)

added_edge_list(adj, 0, 1)
added_edge_list(adj, 0, 2)
added_edge_list(adj, 1, 2)
added_edge_list(adj, 2, 3)

print("\n\n")

for i in range(len(adj)):
    print(f"{i}: ", end="")
    for j in adj[i]:
        print(j, end=" ")
    print()

#!  Graph Çeşitleri

#?       (3)            
#?
#?   (5)     (1)        Null graph : hiç bir kenarı bulunmaz
#?
#?       (4)


#?       (2)            Trivial graph: tek bir düğümden oluşur


#?       (3)            
#?      /    \
#?   (5)      (1)        Undirected graph : Kenarların yönü olmaz
#?      \    /
#?       (4)


#?        (3)            
#?      ↗    ↘
#?   (1)       (2)        Directed graph : Kenarların yönü var
#?      ↘    ↗
#?        (5)


#?       (3)            
#?      /    \
#?   (5)      (1)        Connected graph : Tüm düğümler ziyaret edilebilir
#?      \    /
#?       (4)


#?       (3)            
#?      /    
#?   (5)      (1)         Disconnected graph : En az bir düğüm ziyaret edilemez
#?           /
#?       (4)


#?       (3)            
#?      /    \            K-regular Graph : Her bir düğümün derecesinin k'ya eşit olduğu graph 
#?   (5)      (1)       
#?      \    /            ---> 2-regular Graph çünkü her bir düğüm iki düğüme gidebiliyor
#?       (4)


#?       (3)            
#?      / | \            
#?   (5)-----(1)          Compelete Graph --> Her bir düğümden diğer düğümlere kenarı olan graph
#?      \ | /           
#?       (4)


#?        (3)            
#?      ↗    ↘
#?   (1)       (2)        Cycle graph : Graph kendi içinde dönüyorsa cycle denir
#?      ↖    ↙
#?        (5)


#?        (3)            
#?      ↗    ↘
#?   (1)   ↑   (2)        Cyclic graph : En az bir döngü içermesi
#?           ↙
#?        (5)


#?        (3)            
#?      ↙    ↘
#?   (1)       (2)        Directed acyclic graph : Herhangi bir döngü içermiyor
#?      ↖    ↗
#?        (5)