class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        permutation means set so I need to find if the s1 is in s2
        '''
        
        left = 0
        right = 0
        lens1 = len(s1)
        sorts1 = "".join(sorted(list(s1)))

        while right <= len(s2):
            window = s2[left:right+lens1]
            sorts2 = "".join(sorted(list(window)))

            if sorts1 != sorts2:
                left += 1
                right +=1
            else:
                return True

        return False

            

                





