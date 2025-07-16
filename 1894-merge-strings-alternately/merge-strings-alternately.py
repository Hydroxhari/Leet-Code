class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        m = len(word1)
        n = len(word2)
        loopcount = max(len(word1),len(word2))
        result = ''
        
        for i in range(loopcount):
            if i < m:
                result += word1[i]

            if i < n:   
                result += word2[i]

        return result
        