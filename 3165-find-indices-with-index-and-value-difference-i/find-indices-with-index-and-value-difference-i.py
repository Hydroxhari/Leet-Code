class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
                    ans=[i,j]
                    return ans
        return [-1,-1]
        