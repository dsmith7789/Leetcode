class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = set(["{", "[", "("])
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif len(stack) <= 0:
                return False
            elif ((s[i] == "}" and stack.pop() != "{") or
                 (s[i] == "]" and stack.pop() != "[") or
                 (s[i] == ")" and stack.pop() != "(")):
                return False
        return len(stack) == 0
