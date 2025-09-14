class Solution(object):
    def spellchecker(self, w, q):
        def mask(word):
            return ''.join('*' if ch in 'aeiou' else ch for ch in word.lower())

        # Preprocess
        exact = set(w)
        case_map = {}
        vowel_map = {}
        for word in w:
            lw = word.lower()
            if lw not in case_map:
                case_map[lw] = word
            mw = mask(word)
            if mw not in vowel_map:
                vowel_map[mw] = word

        ans = []
        for query in q:
            if query in exact:
                ans.append(query)
            elif query.lower() in case_map:
                ans.append(case_map[query.lower()])
            elif mask(query) in vowel_map:
                ans.append(vowel_map[mask(query)])
            else:
                ans.append("")
        return ans
