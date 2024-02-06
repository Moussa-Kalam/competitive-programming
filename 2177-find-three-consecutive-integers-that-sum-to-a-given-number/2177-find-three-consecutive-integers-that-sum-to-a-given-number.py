class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        element = (num - 3) / 3
        
        if element.is_integer():
            element = int(element)
            return [element, element + 1, element + 2]
        else:
            return []
        