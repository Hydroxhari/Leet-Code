class Solution(object):
    def maxArea(self, ht):
        
        m=0
        i,j=0,len(ht)-1

        while i<j:
            s=(j-i)*min(ht[i],ht[j])
            m=max(m,s)

            if ht[i]>ht[j]:
                j-=1
            else:
                i+=1
        return m