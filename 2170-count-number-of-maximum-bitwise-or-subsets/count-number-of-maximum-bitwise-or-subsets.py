import heapq
class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # problem formulation:
        #   max_or -> maximum value of bitwise or subset 
        #   return all subsets with max_or 
        # rule: a or b = max -> anything with 
        value_dict = {}
        cur_max = 0
        for num in nums:
            
            cur_dict = value_dict.copy()
            # print(cur_dict)
            if num > cur_max:
                cur_max = num
            if num not in value_dict:
                value_dict[num]=1
            else: value_dict[num]+=1
            for value in cur_dict:
                bitwise_or_value = value|num
                if bitwise_or_value > cur_max:
                    cur_max = bitwise_or_value
                if bitwise_or_value not in value_dict:
                    value_dict[bitwise_or_value] = cur_dict[value]
                else:
                    value_dict[bitwise_or_value] += cur_dict[value]
        return value_dict[cur_max]
        
        # 1: 3
        # 2 2, 2, 2
        
        
        

        