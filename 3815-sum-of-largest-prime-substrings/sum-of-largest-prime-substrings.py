class Solution(object):
    def sumOfLargestPrimes(self, s):

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
        
        u=set()

        for i in range(len(s)):
            for j in range(i,len(s)):
                n=int(s[i:j+1])
                if ip(n):
                    print(n)
                    u.add(n)
        
        l=list(u)
        return sum(sorted(l)[-3:])
        