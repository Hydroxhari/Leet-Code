class Solution(object):
    def divideArray(self, a, k):

        a.sort()
        l=[]
        for i in range(0,len(a)-2,3):
            if a[i+2]-a[i+1]>k or a[i+1]-a[i]>k or a[i+2]-a[i]>k:
                l=[]
                break
            l.append(a[i:i+3])
        return l
        