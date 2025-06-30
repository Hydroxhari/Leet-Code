class Solution(object):
    def minSubArrayLen(self, t, n):

        j=0
        m=float('inf')
        
        cs=0

        for i in range(len(n)):
            cs+=n[i]
            while cs>=t:
                cs-=n[j]
                m=min(m,i-j+1)
                j+=1
            
        return m if m!=float('inf') else 0

        