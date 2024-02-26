class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        while left < right:
            # swap the characters
            s[left], s[right] = s[right], s[left]
            # move the pointers
            left, right = left + 1, right - 1
            
            