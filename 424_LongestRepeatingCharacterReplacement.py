class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letter_count = [0] * 26     # A...Z
        left = 0
        max_length = 0
        for right in range(len(s)):
            # add appropriate count as we move right
            letter_count[ord(s[right]) - ord("A")] += 1
            if (k - sum(letter_count) + max(letter_count)) < 0:
                letter_count[ord(s[left]) - ord("A")] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
