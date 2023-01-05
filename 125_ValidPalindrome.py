class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # my first attempt, but a lot of extra memory
        """
        import string
        from collections import deque

        stack = deque()
        queue = deque()

        for character in s:
            if character not in string.ascii_letters and character not in string.digits:
                continue
            character = character.lower()
            stack.appendleft(character)
            queue.append(character)
        
        while len(stack) > 0:
            if stack.pop() != queue.pop():
                return False
        
        return True
        """

        # use a left and a right pointer for constant extra memory and
        # a more efficient solution

        left = 0
        right = len(s)-1

        while left < right:
            while left < right and self.isAlphaNumeric(s[left]) == False:
                left += 1
            while right > left and self.isAlphaNumeric(s[right]) == False:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isAlphaNumeric(self, character):
        return (ord("A") <= ord(character) <= ord("Z") or
                ord("a") <= ord(character) <= ord("z") or
                ord("0") <= ord(character) <= ord("9"))
