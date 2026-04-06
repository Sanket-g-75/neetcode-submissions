class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join([i.lower() for i in s if i.isascii() and i.isalnum()])
        print(s)
        
        a = False
        if len(s) <= 1:
            return True
        for i in range(len(s)//2):
            if (s[i] == s[len(s) -i -1]):
                i = i+1
                a = True
            else:
                a = False
                break
        return a
            
            
                
            
            
            
        