class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a set of the characters. 
        # If All the characters are same, the sets are same. Return True

        if sorted(s) == sorted(t):
            return True
        else:
            return False
'''
        s_char = []
        t_char = []
        for i in s:
            s_char.append(i)
        for i in t:
            t_char.append(i)

        s_char = set(sorted(s_char))
        t_char = set(sorted(t_char))

        for i in range(len(s_char)):
            if 

'''