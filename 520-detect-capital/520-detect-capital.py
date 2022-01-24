class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
    #or
        return word == word.lower() or word == word.upper() or (word[0] == word[0].upper() and word[1:] == word[1:].lower())