class TrieNode(object):
    def __init__(self) -> None:
        self.children = {} # key = letter, value = TrieNode
        self.isWord = False
        self.refs = 0   # number of times we can use this node
    

    def addWord(self, word):
        current = self
        current.refs += 1
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            current.refs += 1
        current.isWord = True

    def removeWord(self, word):
        current = self
        current.refs -= 1
        for c in word:
            if c in current.children:
                current = current.children[c]
                current.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = set()
        usedSquares = []
        # add words to the trie
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        # helper function
        def dfs(r, c, usedSquares, currentWord, currentNode):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
               (r, c) in usedSquares or
               board[r][c] not in currentNode.children or
               currentNode.children[board[r][c]].refs < 1):
               return None
            letter = board[r][c]
            currentNode = currentNode.children[letter]
            currentWord += letter
            if currentNode.isWord:
                currentNode.isWord = False
                res.add(currentWord)
                root.removeWord(currentWord)
            usedSquares.append((r, c))

            # check neighbors for more words
            dfs(r - 1, c, usedSquares, currentWord, currentNode) # up
            dfs(r + 1, c, usedSquares, currentWord, currentNode) # down
            dfs(r, c - 1, usedSquares, currentWord, currentNode) # left
            dfs(r, c + 1, usedSquares, currentWord, currentNode) # right
            
            # finished exploring so free to explore squares again
            usedSquares.remove((r, c))
            

        # start going through the board
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, usedSquares, "", root)
                if len(res) == len(words):
                    return res
        return res
        
