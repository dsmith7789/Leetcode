class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest_sequence = []
        for num in nums_set:
            if (num - 1) not in nums_set:   # check if start of sequence
                current_sequence = [num]
                while num + 1 in nums_set:  # get length of sequence
                    current_sequence.append(num + 1)
                    num = num + 1
                if len(longest_sequence) < len(current_sequence):   # check if longest sequence
                    longest_sequence = current_sequence
        return len(longest_sequence)
