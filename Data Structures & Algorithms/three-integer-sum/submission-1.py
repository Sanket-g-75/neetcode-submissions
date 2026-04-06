class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums) - 1

            while left < right and right<len(nums):
                print([nums[i],nums[left],nums[right]])
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    if [nums[i],nums[left],nums[right]] not in output:
                        output.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return output


        