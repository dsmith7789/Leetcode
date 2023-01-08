class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in s[left : right]:
                # find and move past duplicate
                while s[left] != s[right]:
                    left += 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
