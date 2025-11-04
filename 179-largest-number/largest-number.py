from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        # Convert to string
        nums = list(map(str, nums))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1  # a before b
            elif a + b < b + a:
                return 1   # b before a
            else:
                return 0
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Edge case: leading zeros (e.g. [0,0])
        ans = ''.join(nums)
        return '0' if ans[0] == '0' else ans
