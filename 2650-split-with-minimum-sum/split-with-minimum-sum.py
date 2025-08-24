class Solution(object):
    def splitNum(self, n):
        s=str(n)
        l=[]
        for i in s:
            l.append(i)
        l.sort()

        o=''
        e=''

        for i in range(0,len(l),2):
            o+=l[i]
            if i+1<len(l):
                e+=l[i+1]
                
        return int(o)+int(e)