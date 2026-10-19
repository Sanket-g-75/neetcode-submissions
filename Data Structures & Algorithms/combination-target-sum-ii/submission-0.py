class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        final = []

        def backtrack(index,path):

            if sum(path) == target:
                final.append(path[:])
                return 
            
            if index >= len(candidates) or sum(path) > target:
               return
           
            path.append(candidates[index])
            backtrack(index+1,path)

            path.pop()

            # Skip duplicates when excluding
            next_index = index + 1
            while (next_index < len(candidates)
                   and candidates[next_index] == candidates[index]):
                next_index += 1
            
            backtrack(next_index,path)
        
        backtrack(0,[])
        return final
        