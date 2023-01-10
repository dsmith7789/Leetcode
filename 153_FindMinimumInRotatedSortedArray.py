class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force, but surprisingly this is faster than 81% of submissions
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]
        """

        # two pointer approach
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] > nums[left + 1]:
                return nums[left + 1]
            if nums[right] < nums[right - 1]:
                return nums[right]
            left += 1
            right -= 1
        return nums[0]
        """

        # binary search -> use concept of left-sorted and right-sorted portions of array
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
