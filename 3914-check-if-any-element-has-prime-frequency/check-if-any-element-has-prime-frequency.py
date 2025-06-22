class Solution(object):
    def checkPrimeFrequency(self, n):

        def ip(n):
            if n<=1:
                return False
            if n<=3:
                return True
            if n%2==0 or n%3==0:
                return False
            for i in range(5,int(n**0.5)+1,6):
                if n%i==0 or n%(i+2)==0:
                    return False
            return True
        
        c=Counter(n)
        for i in c.values():
            if ip(i):
                return True
        return False