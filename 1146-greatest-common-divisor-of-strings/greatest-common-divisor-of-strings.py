class Solution(object):
    def gcdOfStrings(self, s1, s2):
        
        s=''
        l=len(s1)
        sl=len(s2)
        for i in range(1,len(s2)+1):
            cs=s2[:i]
            if cs in s1:
                c=s1.count(cs)
                sc=s2.count(cs)
                if l%len(cs)==0 and sl%len(cs)==0 and sc==(sl//len(cs)) and c==(l//len(cs)):
                    s=cs
        return s
