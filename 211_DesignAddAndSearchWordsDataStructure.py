class TrieNode(object):
    def __init__(self):
        self.children = {} # Hashmap: letter -> TrieNode
        self.endWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.endWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(startIndex, root):
            current = root

            for i in range(startIndex, len(word)):
                letter = word[i]
                if letter == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child) == True:
                            return True
                    return False
                else:
                    if letter not in current.children:
                        return False
                    else:
                        current = current.children[letter]
            return current.endWord
        
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
