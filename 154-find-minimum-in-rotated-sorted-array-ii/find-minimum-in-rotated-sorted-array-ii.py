class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            
            # If duplicates exist, shrink the search space
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[mid] > nums[high]:  # Min must be in the right half
                low = mid + 1
            else:  # Min must be in the left half (including mid)
                high = mid

        return nums[low]