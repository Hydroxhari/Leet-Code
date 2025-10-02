from itertools import combinations
class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()  # Sorting helps in efficient two-pointer checking
        n = len(nums)
        count = 0
        
        # Fix the largest side at index k and use two-pointer method
        for k in range(n - 1, 1, -1):  # Iterate from the last element
            i, j = 0, k - 1  # Two pointers at start and just before k
            
            while i < j:
                if nums[i] + nums[j] > nums[k]:  # Valid triangle condition
                    count += (j - i)  # All pairs (i, j), (i+1, j), ..., (j-1, j) form a valid triangle
                    j -= 1  # Move j to check other possibilities
                else:
                    i += 1  # Increase i to get a larger sum
        
        return count



        