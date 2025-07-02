from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # this will store the increasing subsequence (not necessarily actual subsequence)
        
        for num in nums:
            idx = bisect_left(sub, num)  # find insertion point
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num  # replace to maintain smallest possible tail
                
        return len(sub)
