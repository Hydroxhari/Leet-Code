class Solution(object):
    def nextGreaterElement(self, n, m):

        s=[]
        l=[]
        d=defaultdict(int)
        j=len(m)-1
        for i in m[::-1]:
            d[i]=j
            j-=1
            while s and i>s[-1]:
                s.pop()
            if not s:
                l.append(-1)
            else:
                l.append(s[-1])
            s.append(i)
        l=l[::-1]

        ans=[]
        for i in n:
            ans.append(l[d[i]])
        return ans

        