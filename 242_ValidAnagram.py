class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # "naive" solution
        """
        if len(s) != len(t):
            return False
        s_map = dict()
        t_map = dict()
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 0
            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 0
        for letter in s_map.keys():
            if letter not in t_map.keys():
                return False
            if s_map[letter] != t_map[letter]:
                return False
        return True
        """

        # simpler, but less efficient solution
        return sorted(s) == sorted(t)
        
