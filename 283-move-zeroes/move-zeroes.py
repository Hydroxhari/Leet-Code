class Solution(object):
    def moveZeroes(self, n):

        lp=0
        while lp<len(n):
            if n[lp]==0:
                break
            lp+=1 
        rp=1

        for rp in range(1,len(n)):
            if lp<len(n) and rp>lp and n[lp]==0 and n[rp]!=0:
                n[lp],n[rp]=n[rp],n[lp]
                lp+=1
                while lp<len(n):
                    if n[lp]==0:
                        break
                    lp+=1
            