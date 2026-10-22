
#todo   Trie her bir düğümde bir karekter depoluyor. Bu sayede kelimenin karakterlerini dallara ayırarak saklıyor.
#*      Bu da kelimeleri daha hızlı aramamızı, eklememizi, silmemizi sağlıyor.
#?      Kelimeri karakterleriyle sakladığı için otomatik tamamlama ve doğru yazım kontrolü gibi yapılarda kullanılıyor.

class TrieNode:                         #* karakterleri tutucak children ve son karakteri işaretlicek is_end_of_word field'larına
                                        #* bir TrieNode sınıfı oluşturduk.
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()          #* Trie sınıfını bir TrieNode nesnesi oluşturarak başlattık. 

    def insert(self, word):             #* kelime eklemek için kelimenin karakterlerini dolaşıyoruz.
        node = self.root
        for char in word:
            if char not in node.children:       #* eğer trie da karakter varsa bunun üzerinden ilerliyoruz.
                node.children[char] = TrieNode()
            node = node.children[char]          #* eğer yoksa yeni bir yol oluşturuyoruz.
        node.is_end_of_word = True              #* kelimenin sonuna ulaşınca da true olarak işaretliyoruz.

    def visualize(self, node=None, prefix="", level=0):
        if node is None:                
            node = self.root                                 #? trie içeriğini consol da görebilmek için görselleştirdik 
        for char, child_node in node.children.items():
            print("    " * level + f"|__ {char}")
            if child_node.is_end_of_word:
                print("    " * (level + 1) + "(End of word)")
            self.visualize(child_node, prefix + char, level + 1)

    def search(self, word):                     #? kelime aramak için karakterleri dolaşıyoruz.
        node = self.root
        for char in word:
            if char not in node.children:  
                return False              #* eğer tüm karakterler bulunuyorsa ve son karakter de işaretliyse kelimeyi bulmuş oluyoruz.
            node = node.children[char]
        return node.is_end_of_word

    def start_with(self, prefix):       #* belirli bir örnekle başlayan kelimelerin olup olmadığını kontol etmek için kelimenin
        node = self.root                #* karakterlerine ulaşıyoruz.
        for char in prefix:
            if char not in node.children:    
                return False
            node = node.children[char]
        return True                 #? eğer bu karakterlerin tamamı trie da varsa bu örnekle başlayan kelimenin trie da olduğunu öğreniyoruz

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:                    #? trie da, silmek istediğimiz kelimenin bulunması gerekiyor
                return False
            if depth == len(word):            #? silinecek kelimenin karakterleri başka kelimeler tarafından kullanılıyorsa
                if node.is_end_of_word:        #? bu durumda yalnızca ilgili kelimeyi işaretleyen son işareti kaldırıyoruz.
                    node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char in node.children:
                should_delete_child = _delete(node.children[char], word, depth + 1)
                if should_delete_child:             #? silinecek kelimenin karakterleri başka kelimeler tarafından kullanılmıyorsa
                    del node.children[char]         #? gereksiz düğümleri trie'dan kaldırıyoruz
                return not node.is_end_of_word and len(node.children) == 0
            return False
        _delete(self.root, word, 0)

trie = Trie()

trie.insert("ali")              #* trie'a birkaç kelime ekledik
trie.insert("alp")
trie.insert("alperen")

trie.visualize()

result = trie.search("ali")
print(result)

result = trie.start_with("alper")
print(result)

# trie.delete("ali")
# trie.delete("alp")
trie.delete("alperen")
trie.visualize()