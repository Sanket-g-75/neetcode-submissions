class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        position[i] > position of ith car
        speed[i]    > speed of ith car (in miles per hour)
        
        0-1-2-3-4-5-6-7-8-9-10
              
              C       B     A,D
            C     B     A D
          C   B     A   D

        C B     A     D
        1 2     2     1
        
        '''
        
        pairs = [[p,s] for p,s in zip(position, speed)]

        stack = []

        for p,s in sorted(pairs)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



            


