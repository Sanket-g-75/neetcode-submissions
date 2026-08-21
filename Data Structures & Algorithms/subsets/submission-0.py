class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index,path):

            if index == len(nums):
                results.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()

            backtrack(index+1,path)
    
        results = []
        backtrack(0,[])

        return results