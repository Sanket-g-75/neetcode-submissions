class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ["+","-","*","/"]
        output = None
        
        for i in tokens:
            if len(tokens) == 1 and i not in operators:
                return int(i)
            
            if i not in operators:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                # stack.append(f'({a}{i}{b})')
                if i == "+":
                    result = int(int(a)+int(b))
                    stack.append(result)
                elif i == "-":
                    result = int(int(a)-int(b))
                    stack.append(result)
                elif i == "*":
                    result = int(int(a)*int(b))
                    stack.append(result)
                elif i == "/":
                    result = int(int(a)/int(b))
                    stack.append(result)

        return stack[-1]
            

