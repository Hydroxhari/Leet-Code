class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(t) > len(s):
            return ""
            
        # Count characters in t
        required = Counter(t)
        required_chars = len(required)  # Number of unique characters needed
        
        formed = 0  # Number of unique characters in current window that satisfy requirement
        window = Counter()  # Tracks characters in current window
        
        # Track result
        min_len = float('inf')
        result = ""
        
        left = 0
        for right in range(len(s)):
            # Expand window
            char = s[right]
            window[char] += 1
            
            # Check if this character helps satisfy requirements
            if char in required and window[char] == required[char]:
                formed += 1
            
            # Try to shrink window
            while formed == required_chars:
                # Update result if smaller window found
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                
                # Shrink window
                char = s[left]
                window[char] -= 1
                
                # If removing this character breaks a requirement
                if char in required and window[char] < required[char]:
                    formed -= 1
                    
                left += 1
        
        return result