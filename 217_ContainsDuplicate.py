class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        encountered = dict()
        for i in range(len(nums)):
            key = nums[i]
            if key in encountered:
                return False
            else:
                encountered[key] = 1
        return True
