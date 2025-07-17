class Solution(object):
    def maxArea(self, l):
        i,j=0,len(l)-1
        m=0
        while i<j:
            b=j-i
            h=min(l[i],l[j])
            m=max(m,b*h)
            if l[i]>l[j]:
                j-=1
            else:
                i+=1
        return m