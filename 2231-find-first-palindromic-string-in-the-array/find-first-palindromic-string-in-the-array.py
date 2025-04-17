class Solution(object):
    def firstPalindrome(self, w):

        for i in w:
            if i==i[::-1]:
                return i
        return ''