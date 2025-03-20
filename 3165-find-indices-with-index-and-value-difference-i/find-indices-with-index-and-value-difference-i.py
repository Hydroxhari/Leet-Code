class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        for i in range(len(nums)-indexDifference):
            for j in range(i + indexDifference,len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return[i,j]
        return [-1,-1]
        