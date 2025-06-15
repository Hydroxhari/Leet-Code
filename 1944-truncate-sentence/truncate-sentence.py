class Solution(object):
    def truncateSentence(self, s, k):
        r=s.split()
        return ' '.join(r[:k])