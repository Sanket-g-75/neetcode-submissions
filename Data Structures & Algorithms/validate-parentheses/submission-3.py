class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:
            
            if len(s) == 1:
                return False
            if (len(stack) == 0 and i in [")","}","]"]):
                return False

            if i in ["(","{","["]:
                stack.append(i)
            else:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
        
        
        