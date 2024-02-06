class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt_str = ""
        index = len(s) - 1
        
        while index >= 0:
            if s[index] != "#":
                decrypt_str += chr(96 + int(s[index]))
                index -= 1
            else:
                decrypt_str += chr(96 + int(s[index - 2: index]))
                index -= 3
                
        
        return decrypt_str[::-1]
       
                
        