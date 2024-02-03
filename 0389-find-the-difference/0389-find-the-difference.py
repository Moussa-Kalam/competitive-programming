class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        added_letter = ''
        for character in t:
            if s.count(character) != t.count(character):
                return character
        