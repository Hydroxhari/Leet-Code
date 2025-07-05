class Solution(object):
    def checkSubarraySum(self, nums, k):
        mod_index = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            mod = total % k if k != 0 else total

            if mod in mod_index:
                if i - mod_index[mod] >= 2:
                    return True
            else:
                mod_index[mod] = i
        return False
