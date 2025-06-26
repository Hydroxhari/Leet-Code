class Solution(object):
    def isArraySpecial(self, n):

        for i in range(1,len(n)):
            if (n[i-1]%2==0 and n[i]%2==0) or (n[i-1]%2!=0 and n[i]%2!=0):
                return False
        return True

        