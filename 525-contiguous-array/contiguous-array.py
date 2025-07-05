class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_len = 0
        d = {0: -1}  # base case: sum=0 seen at index -1

        for i in range(len(nums)):
            count += -1 if nums[i] == 0 else 1

            if count in d:
                max_len = max(max_len, i - d[count])
            else:
                d[count] = i

        return max_len
