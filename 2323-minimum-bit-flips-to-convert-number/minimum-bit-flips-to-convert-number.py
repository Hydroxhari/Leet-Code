class Solution(object):
    def minBitFlips(self, s, g):

        c=s^g
        return bin(c).count('1')