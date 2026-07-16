class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Same as the prev one but here I will have to minus the m from the target as well
        '''
        l = 0
        r = len(nums) -1
        
        while l <=r:
            m =(l+r)//2

            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r= m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r= m-1
                else:
                    l= m+1
        return -1
                