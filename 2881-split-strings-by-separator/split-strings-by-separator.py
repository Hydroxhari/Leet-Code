class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        words=" ".join(words)
        return words.replace(separator," ").split()
        
        
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        