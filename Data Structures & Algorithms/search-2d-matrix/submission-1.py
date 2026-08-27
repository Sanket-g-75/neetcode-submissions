class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # In this can' I directly flatten the list 

        nums = None
        for i in matrix:
            if nums is None:
                nums =  i
            else:
                nums.extend(i)

        l = 0
        r = len(nums)-1

        while l <=r:
            mid =  (l+r)//2

            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                r = mid -1
            elif target > nums[mid]:
                l = mid + 1
        return False
            
            