class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        len_nums = len(nums)

        record_left_ptr, record_right_ptr = 0, indexDifference

        record_max_val, record_min_val = (-1), ((10 ** 9) + 1)

        while (record_right_ptr < len_nums):
            if (nums[record_left_ptr] > record_max_val):
                record_max_val, record_max_idx = nums[record_left_ptr], record_left_ptr
            else:
                pass

            if (nums[record_left_ptr] < record_min_val):
                record_min_val, record_min_idx = nums[record_left_ptr], record_left_ptr
            else:
                pass

            if (abs((nums[record_right_ptr] - record_max_val)) >= valueDifference):
                return [record_max_idx, record_right_ptr]
            else:
                pass

            if (abs((nums[record_right_ptr] - record_min_val)) >= valueDifference):
                return [record_min_idx, record_right_ptr]
            else:
                pass

            record_left_ptr += 1
            record_right_ptr += 1

        return [(-1), (-1)]