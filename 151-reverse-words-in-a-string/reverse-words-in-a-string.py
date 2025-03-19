class Solution(object):
    def reverseWords(self, s):
        l=s.split()
        return ' '.join(l[::-1])
        