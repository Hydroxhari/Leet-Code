class Solution(object):
    def candy(self, l):

        r=[1]*len(l)

        for i in range(1,len(l)):
            if l[i]>l[i-1]:
                r[i]=r[i-1]+1

        for i in range(len(l)-2,-1,-1):
            if l[i]>l[i+1]:
                r[i]=max(r[i],r[i+1]+1)
        
        return sum(r)
