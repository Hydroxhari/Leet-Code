import math

class Solution(object):
    def replaceNonCoprimes(self, n):
        s = []
        for i in n:
            while s and math.gcd(s[-1], i) > 1:
                i = math.lcm(s.pop(), i)
            s.append(i)
        return s
