class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        paths = []

        def explore(path, i, nums):
            if i == len(nums):
                # if there's no more elements to consider, we have a valid subset
                paths.append(path)
                return
            else:
                # for each element, we can either include it or exclude it, so explore both options
                include = path.copy()
                include.append(nums[i])
                exclude = path.copy()
                explore(include, i + 1, nums)
                explore(exclude, i + 1, nums)
        
        explore([], 0, nums)
        return paths
