class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        (This solution is correct but is a bit time consuming)

        results = []

        for i in range(len(temperatures)):

            window = temperatures[i:]
            
            if temperatures[i] >= max(window):
                results.append(0)
                continue

            for j in range(len(window)):
                if window[j] > temperatures[i]:
                    results.append(j)
                    break
                else:
                    continue
                    

        if len(results) <= len(temperatures):
            extras = len(temperatures) - len(results)
            results.extend([0]*extras)

        return results
        '''

        results = [0]*len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                results[stackInd] = (i-stackInd)
            stack.append([temp, i])
        
        return results


        