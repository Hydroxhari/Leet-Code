class Solution(object):
    def countCharacters(self, w, c):

        c=Counter(c)
        s=0
        print(c)

        for i in w:
            if c&Counter(i)==Counter(i):
                s+=len(i)
        return s
