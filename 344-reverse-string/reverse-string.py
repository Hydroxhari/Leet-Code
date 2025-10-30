class Solution(object):
    def reverseString(self, s):

        j=len(s)-1
        for i in range(len(s)//2):
            s[i],s[j]=s[j],s[i]
            j-=1
        
