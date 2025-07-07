from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        count = Counter(digits)
        res = []
        
        for num in range(100, 1000, 2):  # Only 3-digit EVEN numbers
            c = Counter(map(int, str(num)))
            if all(count[d] >= c[d] for d in c):
                res.append(num)
        
        return res
