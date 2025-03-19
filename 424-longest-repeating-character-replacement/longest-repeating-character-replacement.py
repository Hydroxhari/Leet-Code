class Solution(object):
    def characterReplacement(self, s, k):
        freq = defaultdict(int)
        maxFreq = 0
        i = 0  
        for j, n in enumerate(s):
            freq[n] += 1
            if freq[n] > maxFreq: 
                maxFreq = freq[n]
            if (j-i+1) - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
        return j-i+1

        