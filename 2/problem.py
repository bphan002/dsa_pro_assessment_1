class Solution:
    def processData(self, data_processing_capacity, target):
        # 2 sliding window
        left = 0
        curr_capacity = 0 #2
        min_capacity = float('inf')

        for right, capacity in enumerate(data_processing_capacity):
            curr_capacity += capacity
            while curr_capacity >= target:
                min_capacity = min(min_capacity, right - left + 1)
                curr_capacity -= data_processing_capacity[left]
                left +=1

        if min_capacity == float('inf'):
            return 0
        else: 
            return min_capacity
