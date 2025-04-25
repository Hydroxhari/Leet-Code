from functools import lru_cache

class Solution:
    def minDistance(self, w: str, t: str) -> int:

        l, k = len(w), len(t)

        @lru_cache(None)  # Memoization cache
        def dfs(i, j):
            # Base cases
            if i == l:  # If we have exhausted all characters in w
                return k - j  # We need to insert the remaining characters of t
            if j == k:  # If we have exhausted all characters in t
                return l - i  # We need to delete the remaining characters of w
            
            # If characters match, no operation needed, move to the next characters
            if w[i] == t[j]:
                return dfs(i + 1, j + 1)

            # Otherwise, calculate the minimum number of operations (insert, delete, replace)
            delete = dfs(i + 1, j)  # Deleting a character from w
            insert = dfs(i, j + 1)  # Inserting a character into w (i.e., matching it to t)
            replace = dfs(i + 1, j + 1)  # Replacing a character in w with the one in t

            return 1 + min(delete, insert, replace)  # Add 1 for the current operation

        # Start from the beginning of both strings
        return dfs(0, 0)
