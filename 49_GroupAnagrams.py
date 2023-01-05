class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # slow runtime, less memory used
        """
        sort_map = dict() # sorted_word : list of original words
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in sort_map.keys():
                anagram_group = sort_map[sorted_word]
                anagram_group.append(word)
            else:
                anagram_group = [word]
                sort_map[sorted_word] = anagram_group
        return sort_map.values()
        """
        # faster run time because don't rely on sorting algorithm
        # instead count occurrences of each letter and store that as the 
        # key in the hashmap
        # more memory used because the 26 byte array for each word in strs
        from collections import defaultdict
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26 # only the 26 lowercase characters are used
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            res[tuple(count)].append(word)
        return res.values()


