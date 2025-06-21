class Solution(object):
    def generateTag(self, c):
        s='#'
        l=c.split()
        if not l:
            return '#'
        s+=lower(l[0])
        for i in l[1:]:
            s+=i.title()
        return s[:100]