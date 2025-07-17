class Solution(object):
    def isPossible(self,nums):
        freq = Counter(nums)  # frequency of each number
        need = Counter()      # how many subsequences need a specific number

        for num in nums:
            if freq[num] == 0:
                continue  # already used

            # Case 1: Extend a previous subsequence
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
                freq[num] -= 1

            # Case 2: Start a new subsequence
            elif freq[num+1] > 0 and freq[num+2] > 0:
                freq[num] -= 1
                freq[num+1] -= 1
                freq[num+2] -= 1
                need[num + 3] += 1

            # Case 3: Not possible
            else:
                return False

        return True


        