class Solution(object):
    def findTheDistanceValue(self, a1, a2, d):
        it=False
        c=0
        for i in a1:
            for j in a2:
                if abs(i-j)<=d:
                    it=True
                    break
            if not it:
                c+=1
            it=False
        return c


        