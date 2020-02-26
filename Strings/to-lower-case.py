class Solution:
    def toLowerCase(self, str: str) -> str:
        output = ""
        for i in str:
            output += i.lower()
        
        return output