class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','[':']','{':'}'}
        
        class my_stack:
            def __init__(self):
                self.arr = []
                
            def push(self,var):
                self.arr.append(var)
                
            def pop(self):
                if not self.arr:
                    print("list is empty")
                    return 0
                
                val = self.arr.pop()
                return val
            
        obj = my_stack()
        
        if len(s) == 0:
            return True
        
        if len(s) % 2 ==1 :
            return False
        
        elif len(s)%2==0:
            for item in s:
                if item in d.keys():
                    obj.push(item)
                
                elif item in d.values():
                    val = obj.pop()
                    if val == 0:
                        return False
                    if d[val] == item:
                        continue
                    else:
                        return False
                
            if obj.arr:
                return False
        
            return True