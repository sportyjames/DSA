class Solution:

    # Quicksort Time Complexity:
    #average: O(nlogn)
    # worst: O(n^2) when selected pivot is the maximum or minimum, causing one side has partition of n - 1 element

    def quicksort(self, array):
        self.helper(array, 0, len(array) - 1)
        return array

    # average T: O(logn)
    # worst T: O(n)
    def helper(self, array, left, right):
        if left >= right:
            return
        partition_idx = self.partition(array, left, right)
        self.helper(array, left, partition_idx - 1)
        self.helper(array, partition_idx + 1, right)

    def swap(self, array, left, right):
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp

    #T: O(N)
    def partition(self, array, left, right):
        # make pivot the last element of the array
        pivot_val = array[right]
        start = left
        end = right - 1

        while start <= end:
            if array[start] <= pivot_val:
                # keep moving start
                start += 1
            elif array[end] > pivot_val:
                # keep moving end
                end -= 1
            else:
                # stop moving at this time
                # swap start wtih end
                # also update their index
                self.swap(array, start, end)
                start += 1
                end -= 1

        # swap start with pivot index
        self.swap(array, start, right)

        # return start's position as partition index
        return start


sol = Solution()
print(sol.quicksort([10, 80, 30, 90, 40, 50, 70]))
