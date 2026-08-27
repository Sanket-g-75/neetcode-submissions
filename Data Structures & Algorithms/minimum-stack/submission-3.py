class MinStack:

    def __init__(self):
        self.stack = []
        self.nums = []

    def push(self, val: int) -> None:
        self.stack.append(val) 

        if (isinstance(val, int)) or (isinstance(val,float)):    
            val = min(val, self.nums[-1] if self.nums else val)
            self.nums.append(val)
            
    def pop(self) -> None:
        self.nums.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.nums[-1]

        
