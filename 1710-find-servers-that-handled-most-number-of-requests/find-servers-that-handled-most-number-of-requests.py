from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        freq = [0]*k
        busy = [] # min-heap 
        free = SortedList(range(k)) # balanced bst
        
        for i, (ta, tl) in enumerate(zip(arrival, load)): 
            while busy and busy[0][0] <= ta: 
                _, ii = heappop(busy)
                free.add(ii)
            
            if free: 
                ii = free.bisect_left(i%k) % len(free)
                server = free.pop(ii)
                freq[server] += 1
                heappush(busy, (ta+tl, server))
        
        mx = max(freq)
        return [i for i, x in enumerate(freq) if x == mx]