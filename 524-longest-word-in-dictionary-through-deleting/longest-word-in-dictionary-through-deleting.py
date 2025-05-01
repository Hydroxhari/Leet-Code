class Solution(object):
    def findLongestWord(self, s, d):
        def is_subsequence(x, y):
            # Check if x is a subsequence of y
            it = iter(y)
            return all(c in it for c in x)

        longest = ""
        for word in d:
            if is_subsequence(word, s):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest
