class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # is left of mid sorted?
            if nums[l] <= nums[m]:
                if target > nums[l] and target < nums[m]: # we know for sure it will be in left
                    r = m - 1
                else: # we know for sure it's definitely not in the left
                    l = m + 1
            else:   # if left is not sorted, then right of mid must be sorted
                if target > nums[m] and target < nums[r]: # we know for sure it's in right side
                    l = m + 1
                else: # we know for sure it's definitely not in the right
                    r = m - 1
        return -1
