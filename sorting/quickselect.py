class Solution:
    
    #Quickselect: it is a selection algorithm to find the kth smallest element in an unorder list. It is related to the quick sort algorithm
    #T: O(N) in the average case
    #S: O(1)
    
    def findKthLargest(self, nums, k):
        self.helper(nums, 0, len(nums) - 1, k)
        return nums[len(nums) - k]
        
    def helper(self, nums, left, right, k):
        if left >= right:
            return 

        partitionIdx = self.partition(nums, left, right)
        #we found the res 
        if partitionIdx == len(nums) - k:
            return
        elif partitionIdx < len(nums) - k:
            self.helper(nums, partitionIdx + 1, right, k)
        else:
            self.helper(nums, left, partitionIdx - 1, k)
    
    def swap(self, nums, left, right):
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
    
    def partition(self, nums, left, right):
        pivotVal = nums[right]
        start = left
        end = right - 1
        
        while start <= end:
            if nums[start] <= pivotVal:
                start += 1
            elif nums[end] > pivotVal:
                end -= 1
            else:
                self.swap(nums, start, end)
                start += 1
                end -= 1
        
        self.swap(nums, start, right)
        return start
                
        