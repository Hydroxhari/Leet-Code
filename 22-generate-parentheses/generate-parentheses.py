class Solution(object):
    def generateParenthesis(self, n):

        l=[]

        def b(s,o,c):
            if len(s)==n*2:
                l.append(s)
                return
            
            if o<n:
                b(s+'(',o+1,c)
            
            if c<o:
                b(s+')',o,c+1)

        b('',0,0)
        return l
