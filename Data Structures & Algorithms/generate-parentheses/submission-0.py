class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []

        def complete(path):
            stack = []
            for char in path:
                if char == '(':
                    stack.append(char)
                else:
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                if complete(path):
                    final.append("".join(path))
                return

            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()

            if close_count < n:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return final