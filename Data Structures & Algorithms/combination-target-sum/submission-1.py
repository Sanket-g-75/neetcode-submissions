class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        path = []

        def backtrack(index, remaining):
            if remaining == 0:
                final.append(path.copy())
                return

            if index == len(nums) or remaining < 0:
                return

            # Include the current number
            path.append(nums[index])
            backtrack(index, remaining - nums[index])

            # Backtrack: remove the current number
            path.pop()

            # Skip the current number
            backtrack(index + 1, remaining)

        backtrack(0, target)
        return final