class Solution(object):
    def longestSubsequence(self, s, k):

        j=len(s)
        c=''
        cc=0
        for i in range(len(s)-1,-1,-1):
            c=s[i]+c
            if int(c,2)>k:
                j-=1
                break
            j-=1
            cc+=1
        
        for i in range(0,j):
            if s[i]=='0':
                cc+=1
        return cc
