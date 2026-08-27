class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # So I have to find the minimum no. of bananas/hours so that the eating completes inside the timing

        '''
        So first I will have to find out what can be the max. k
        So as this is a list, max is not known as lists have no metadata, so first I will have to find the max
        for which I will have to use the binary search
        '''

        def ttaken(lst,h):

            counter = 0

            for i in lst:
                
                if  i%h == 0:
                    counter += int(i/h)
                else:
                    counter += int(i/h) + 1
            
            return counter
        l = 1
        r = max(piles)
        result = 1000000000
        
        while l <= r:
            
            m = (l + r)//2
            tm = ttaken(piles,m)

            if tm > h:
                l = m +1
            elif tm <= h:
                result = min(result,m)
                r = m-1
        return result
            

        

            



        