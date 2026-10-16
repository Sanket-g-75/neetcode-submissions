class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq

        heap = []
        final = []

        for x,y in points:
            dist = (x**2) + (y**2)
            heap.append([dist,x,y])
        
        heapq.heapify(heap)

        while k > 0:
            dist,x,y = heapq.heappop(heap)
            final.append([x,y])
            k -=1
        
        return final
            


        

        