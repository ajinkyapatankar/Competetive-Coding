# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(nested,res):
            if nested.isInteger():
                res.append(nested.getInteger())
            else:
                nestedlist = nested.getList()
                for l in nestedlist:
                    flatten(l,res)
        self.main_res = []
        for l in nestedList:
            flatten(l,self.main_res)
        self.i = 0
        

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.main_res[self.i-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.main_res)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())