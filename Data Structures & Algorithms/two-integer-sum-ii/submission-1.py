class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Array is in increasing order
        for i in range(len(numbers)):
            j = i+1
            while j <len(numbers):
                print(i,j)
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                else:
                    j +=1
                

            
        