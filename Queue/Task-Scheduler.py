class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fre = {}
        for task in tasks:
            if task not in fre:
                fre[task] = 1
            else:
                fre[task] += 1
                
        max_count = 0
        max_value = max(fre.values()) 
        for value in fre.values():
            if value == max_value:
                max_count += 1
        
        return max(len(tasks),(max_value-1)*(n+1) + max_count)