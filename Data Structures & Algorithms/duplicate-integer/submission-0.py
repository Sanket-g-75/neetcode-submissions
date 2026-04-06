class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        result = False

        for i in nums:
            if i not in dictionary.keys():
                dictionary[i] = 1
            else:
                dictionary[i] += 1

        for i in dictionary.values():
            if i > 1:
                result = True
        return result