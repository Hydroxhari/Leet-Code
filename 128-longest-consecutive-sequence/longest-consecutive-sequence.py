class Solution(object):
    def longestConsecutive(self, n):
        n.sort()
        if not n:
            return 0
        c=0
        m=0
        for i in range(1,len(n)):
            if n[i]==n[i-1]:
                continue
            elif n[i]==n[i-1]+1:
                c+=1
                m=max(m,c)
            else:
                c=0
        return m+1