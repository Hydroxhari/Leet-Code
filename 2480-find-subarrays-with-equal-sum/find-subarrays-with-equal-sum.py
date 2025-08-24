class Solution(object):
    def findSubarrays(self, n):

        s=set()
        for i in range(len(n)-1):
            cs=n[i]+n[i+1]
            if cs in s:
                return True
            s.add(cs)
        return False