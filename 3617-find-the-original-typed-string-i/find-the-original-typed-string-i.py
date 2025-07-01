class Solution(object):
    def possibleStringCount(self, word):
        n = 1
        for i in range (1, len(word)) :
            if word[i]==word[i-1] :
                n +=1
        return n        