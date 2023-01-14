class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()     

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if current.children[index] == None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.endWord = True           
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if current.children[index]:
                current = current.children[index]
            else:
                return False
        return current.endWord

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            index = ord(letter) - ord("a")
            if current.children[index]:
                current = current.children[index]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
