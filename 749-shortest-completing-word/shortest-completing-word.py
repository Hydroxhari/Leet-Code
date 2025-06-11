from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        # Create frequency map for license plate
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        result = None

        for word in words:
            word_counter = Counter(word)

            # Check if word satisfies all required letters
            if all(word_counter[char] >= count for char, count in required.items()):
                if result is None or len(word) < len(result):
                    result = word

        return result
