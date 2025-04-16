class Solution(object):
    def removeDuplicates(self, n):
        s=set(n)
        n[:] = []  
        for i in s:
            n.append(i)
        n.sort()

            
        