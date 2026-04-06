class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}

        for i in nums:
            if i not in elements.keys():
                elements[i] = 1
            else:
                elements[i] += 1
        
        elements = dict(sorted(elements.items(),key = lambda x: x[1],reverse=True)[:k])

        return list(elements.keys())


        