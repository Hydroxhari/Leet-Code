class Solution(object):
    def isPalindrome(self, s):

        n=''
        for i in s:
            if i.isalpha():
                n+=lower(i)
            elif i.isdigit():
                n+=i
        return n==n[::-1]