class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. sort the array to help skip duplicates

        # 2. choose a fixed number

        # 3. fixed number is the target and 
        # can approach this like Two Sum II

        res = []
        nums.sort()

        for i, fixed in enumerate(nums):
            if i > 0 and fixed == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = fixed + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([fixed, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
