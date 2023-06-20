# Try data structure for word prefix lookup

class TrieNode:
    def __init__(self, s):
        self.string = s
        self.is_word = False

        # Dictionary to store children of form char: node
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, string: str):
        node = self.root

        for char in string:
            # If the node doesnt exist, create one
            if char not in node.children:
                node.children[char] = TrieNode(node.string + char)
            
            # Continue down the trie
            node = node.children[char]
    
        # The last node created / visited corresponds to the end of a word
        node.is_word = True
    
    def lookup(self, prefix: str):
        # Returns true if a given prefix exists in the trie
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return True
    
    def is_word(self, string: str) -> bool:
        # Returns true if the given string is a word in the trie
        node = self.root

        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return node.is_word
    
if __name__ == "__main__":
    trie = Trie()

    words = ["wood", "trees", "tree", "bark"]
    for word in words:
        trie.insert(word)

    print(trie.lookup("c"))
    print(trie.is_word("wood"))
