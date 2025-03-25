class Solution(object):
    def findTheDistanceValue(self, a1, a2, d):
        
        def bt(a,i):
            l,r=0,len(a)-1
            while l<=r:
                m=(l+r)//2
                if abs(a[m]-i)<=d:
                    return False
                if a[m]>i:
                    r=m-1
                else:
                    l=m+1
            return True



        a2.sort()
        c=0
        for i in a1:
            if bt(a2,i):
                c+=1
        return c


        