class Solution(object):
    def getLucky(self, s, k):

        r=''
        for i in s:
            r+=str(ord(i)-96)
        
        for i in range(k):
            s=0
            for j in r:
                s+=int(j)
            r=str(s)

        return int(r)