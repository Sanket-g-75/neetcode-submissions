class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        '''
        The array is sorted in increasing order, so I can use a left most pointer and
        run a pointer from left+1 to right most position but that will take O(n^2) time. 
        So instead of that I can use a right pointer and if the left pointer is same as right pointer,
        I will remove the left pointer and move it forward

        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[right] == nums[right-1]:
                nums.pop(right)
            right -=1
            
        
        return len(nums)
        