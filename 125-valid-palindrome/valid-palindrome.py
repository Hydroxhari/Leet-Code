class Solution(object):
    def isPalindrome(self, s):
        r=''
        for i in s:
            if i.isalnum():
                r+=i.lower()
        return r==r[::-1]

        