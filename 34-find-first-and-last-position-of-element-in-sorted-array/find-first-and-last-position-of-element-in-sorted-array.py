class Solution(object):
    def searchRange(self, nums,target):
        first =self.findFirst(nums, target)
        last =self.findLast(nums, target)
        return [first, last]

    def findFirst(self, nums,target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def findLast(self, nums,target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
                
            
        