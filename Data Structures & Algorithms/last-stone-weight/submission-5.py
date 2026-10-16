class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        for i in range(len(stones)):
            stones[i] = -stones[i]
        

        
        heapq.heapify(stones)

        if len(stones) == 1:
            return -stones[0]

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(stones,y-x)
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
        