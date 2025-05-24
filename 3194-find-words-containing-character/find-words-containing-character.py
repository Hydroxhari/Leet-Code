class Solution(object):
    def findWordsContaining(self, w, x):

        l =[]
        j=-1
        for i in w:
            j+=1
            if x in i:
                l.append(j)
        return l