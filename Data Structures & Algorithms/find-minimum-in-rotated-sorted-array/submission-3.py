class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        What I can do is I can apply binary search on the indexes and then compare values 
        based on nums[idx]
        '''
        l = 0
        r = len(nums) -  1
        minimum = min(nums[l],nums[r])

        while l <= r:
            m = (l+r)//2
            diffleft = nums[m] -  nums[l]
            diffright = nums[m] - nums[r]
            minimum= min(minimum,nums[m])
            if abs(diffright) > abs(diffleft):
                l = m+1
            else:
                r  = m-1
        return minimum
