class Solution(object):
    def triangleType(self, n):
        # Sort the sides for easier triangle inequality check
        n.sort()
        
        # Check triangle validity: sum of two smallest > the largest
        if n[0] + n[1] <= n[2]:
            return 'none'
        
        unique_sides = len(set(n))
        
        if unique_sides == 1:
            return 'equilateral'
        elif unique_sides == 2:
            return 'isosceles'
        else:
            return 'scalene'
