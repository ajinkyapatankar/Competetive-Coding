from heapq import heappush, heappop
from collections import Counter, deque
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or k == 1:
            return s
        counter = Counter(s)
        heap = []; queue = deque()
        ans = ''
        
        for ch, freq in counter.items():
            heappush(heap, (-freq, ch))
        
        while heap:
            freq, ch = heappop(heap)
            ans += ch
            queue.append((freq+1, ch))
            if len(queue) == k:
                freq, ch = queue.popleft()
                if -freq>0:
                    heappush(heap, (freq, ch))
        return ans if len(ans) == len(s) else ''