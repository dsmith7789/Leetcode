class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 1. find starting letter

        def valid(start, usedSquares, i):
            if i == len(word):
                return True

            letter = word[i]
            # check up square
            if start[0] > 0 and (start[0] - 1, start[1]) not in usedSquares and board[start[0] - 1][start[1]] == letter:
                newStart = (start[0] - 1, start[1])
                snapshot = usedSquares.copy()
                usedSquares.append(newStart)
                if valid(newStart, usedSquares, i + 1) == True:
                    return True
                else:
                    usedSquares = snapshot
            # check down square
            if start[0] < len(board) - 1 and (start[0] + 1, start[1]) not in usedSquares and board[start[0] + 1][start[1]] == letter:
                newStart = (start[0] + 1, start[1])
                snapshot = usedSquares.copy()
                usedSquares.append(newStart)
                if valid(newStart, usedSquares, i + 1) == True:
                    return True
                else:
                    usedSquares = snapshot
            # check left square
            if start[1] > 0 and (start[0], start[1] - 1) not in usedSquares and board[start[0]][start[1] - 1] == letter:
                newStart = (start[0], start[1] - 1)
                snapshot = usedSquares.copy()
                usedSquares.append(newStart)
                if valid(newStart, usedSquares, i + 1):
                    return True
                else:
                    usedSquares = snapshot
            # check right square
            if start[1] < len(board[0]) - 1 and (start[0], start[1] + 1) not in usedSquares and board[start[0]][start[1] + 1] == letter:
                newStart = (start[0], start[1] + 1)
                snapshot = usedSquares.copy()
                usedSquares.append(newStart)
                if valid(newStart, usedSquares, i + 1):
                    return True
                else:
                    usedSquares = snapshot
            
            return False
        
        # 3. repeat the check until we've used all the letters from the word
        board_letter_count = {}
        word_letter_count = {}
        for c in word:
            word_letter_count[c] = 1 + word_letter_count.get(c, 0)
        for row in range(len(board)):
            for col in range(len(board[0])):
                c = board[row][col]
                board_letter_count[c] = 1 + board_letter_count.get(c, 0)
        for c in word_letter_count.keys():
            if word_letter_count[c] > board_letter_count.get(c, 0):
                return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if len(word) == 1:
                        return True
                    # 2. from starting letter, check if any adjacents are the next letter
                    start = (row, col)
                    usedSquares = [start]
                    found = valid(start, usedSquares, 1)
                    if found:
                        return True
        return False
