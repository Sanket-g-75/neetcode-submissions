class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []

        def backtrack(path):
            if len(path) == len(nums):
                final.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return final