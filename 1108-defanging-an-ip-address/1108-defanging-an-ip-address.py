class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = ''
        
        for character in address:
            if character == ".":
                defang += "[.]"
            else:
                defang += character
                
        return defang
        