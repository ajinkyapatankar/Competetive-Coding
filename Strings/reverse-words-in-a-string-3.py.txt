class Solution:
     def reverseWords(self, s: str) -> str:
        new_s = ""
        wordList = s.split(" ")
        for word in wordList[:-1]:
            new_word = word[::-1]
            new_s += new_word
            new_s += " "
            
        new_s += wordList[-1][::-1]
            
        return new_s
   