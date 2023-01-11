class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force is checking every combination -> O(n^2) complexity -> bad
        # better is to use hash map to store values and indexes
        # add values to hash map as we go through the array

        nums_map = dict()
        for i in range(len(nums)):
            current = nums[i]
            lookup = target - current
            index = nums_map.get(lookup, -1)
            if index != -1:
                return i, index
            else:
                nums_map[current] = i

