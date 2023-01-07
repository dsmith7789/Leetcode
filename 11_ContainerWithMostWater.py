class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # brute force: check every combination; O(n^2) run complexity
        """
        maxArea = -1
        for i in range(len(height)):
            for j in range(len(height)):
                w = abs(i - j)
                h = min(height[i], height[j])
                area = w * h
                maxArea = max(area, maxArea)
        return maxArea
        """

        # two pointers; O(n) run complexity
        maxArea = -1
        left, right = 0, len(height) - 1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            maxArea = max(area, maxArea)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            elif height[left + 1] > height[right - 1]:
                left += 1
            else:
                right -= 1
        return maxArea

