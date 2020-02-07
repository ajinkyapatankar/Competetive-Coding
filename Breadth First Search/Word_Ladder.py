class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if len(beginWord) != len(endWord) or not beginWord or not endWord or not wordList:
            return 0
        
        dic = collections.defaultdict(list)
        
        for word in wordList:
            if len(word) != len(beginWord):
                continue
            for i in range(len(word)):
                dic[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = [(beginWord,1)]
        visited = set()
        visited.add(beginWord)
        
        while queue:
            w,dis = queue.pop(0)
            for i in range(len(w)):
                temp = w[:i] + '*' + w[i+1:]
                for nextword in dic[temp]:
                    if nextword not in visited:
                        if nextword == endWord:
                            return dis + 1
                        
                        queue.append((nextword,dis+1))
                        visited.add(nextword)
                        
        return 0
        
        
        