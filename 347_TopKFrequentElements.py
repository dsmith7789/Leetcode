class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_counts = dict() # key = number, value = count
        occurrence_array = [[] for i in range(len(nums) + 1)]

        # count up how many times each number is in the array
        for num in nums:
            num_counts[num] = 1 + num_counts.get(num, 0)
            
        # store the counts in occurrence_array so we can 
        # efficiently retrieve top occurring numbers
        for num, count in num_counts.items():
            occurrence_array[count].append(num)
        
        # loop through occurrence_array backwards until we've found
        # the k most frequent elements
        output_array = []
        for i in range(len(occurrence_array)-1, -1, -1):
            for num in occurrence_array[i]:
                output_array.append(num)
                if len(output_array) == k:
                    return output_array

