class Solution(object):
    def numberOfSubarrays(self, n, k):

        def atm(k):
            j=0
            c=0
            for i in range(len(n)):
                if n[i]%2!=0:
                    k-=1
                
                while k<0:
                    if n[j]%2!=0:
                        k+=1
                    j+=1
                
                c+=(i-j+1)
            return c
            
        return atm(k)-atm(k-1)
