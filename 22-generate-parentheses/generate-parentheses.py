class Solution(object):
    def generateParenthesis(self, n):

        l=[]

        def bt(s,o,c):
            if len(s)==2*n:
                l.append(s[:])
                return
            
            if o>0 and o<=c:
                bt(s+'(',o-1,c)
            if c>o:
                bt(s+')',o,c-1)
        
        bt('',n,n)
        return l