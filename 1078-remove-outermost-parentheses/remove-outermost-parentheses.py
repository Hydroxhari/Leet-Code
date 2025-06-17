class Solution(object):
    def removeOuterParentheses(self, s):
        o=0
        c=0
        l=''
        for i in s:

            if i=='(':
                if not o:
                    o+=1
                    continue
                o+=1
                l+='('
            else:
                o-=1
                if o:
                    l+=')'
        return l

