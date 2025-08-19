class Solution(object):
    def zeroFilledSubarray(self, n):

        c=0
        i=0
        while i<len(n):
            if n[i]==0:
                j=i
                while j<len(n) and n[j]==0:
                    c+=j-i+1
                    j+=1
                i=j
            i+=1
        return c
                    
        