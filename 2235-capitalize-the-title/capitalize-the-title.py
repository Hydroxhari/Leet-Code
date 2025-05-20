class Solution(object):
    def capitalizeTitle(self, t):
        t=t.split()
        s=''
        for i in t:
            if len(i)>2:
                s+=capitalize(i) + ' '
            else:
                s+=lower(i)+' '
        return s[:-1] if s else ''