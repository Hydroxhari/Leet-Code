class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) // 2

            print(nums[m])
            if nums[m] == target:
                return m

            if nums[m] >= nums[s]:  # Left sorted
                if nums[s] <= target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:  # Right sorted
                if nums[m] < target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1

        return -1