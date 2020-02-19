class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        
        pairset = set(map(tuple,pairs))
        
        return all(w1==w2 or (w1,w2) in pairset or (w2,w1) in pairset for w1,w2 in zip(words1,words2))