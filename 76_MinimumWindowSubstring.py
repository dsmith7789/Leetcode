class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 2 hashmaps
        # 1 for the count of letters in t
        # 1 for the substring of s[left : right] but the only keys are the letters from t
        # increment the count of the letter at right if it's in the hashmap keys
        # if we need to move left, decrement the count of the value we moved it off
        # once we find a valid window, shrink by finding the next element in the window

        t_map = {}
        for letter in t:
            t_map[letter] = 1 + t_map.get(letter, 0)
        substring_map = dict.fromkeys(t_map, 0)
        left = 0
        min_substring = ""
        for right in range(len(s)):

            # 1. move right and increment the appropriate keys
            if s[right] in t_map.keys():
                substring_map[s[right]] = 1 + substring_map.get(s[right], 0)
            # 2. move left to shrink window if needed, to place it on a valid (and non-bonus) letter
            # decrement counts as appropriate
            while (
                    left <= right) and \
                    (
                        (s[left] not in t_map) or 
                        (substring_map[s[left]] > t_map[s[left]])
                    ):
                if s[left] in substring_map:
                    substring_map[s[left]] -= 1
                left += 1

            # 3. if the window is valid, check if we can replace the min_substring
            if all(substring_map[k] >= t_map[k] for k in t_map):
                if min_substring == "":
                    min_substring = s[left : right + 1]
                elif right - left < len(min_substring):
                    min_substring = s[left : right + 1]
                substring_map[s[left]] -= 1
                left += 1       

        return min_substring
