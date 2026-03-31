class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}': '{', ')': '(', ']': '['}

        for char in s:
            if char in mapping:              # closing bracket
                if stack and stack[-1] == mapping[char]:  # top matches?
                    stack.pop()
                else:
                    return False             # mismatch or empty stack
            else:
                stack.append(char)           # opening bracket → push

        return len(stack) == 0

# Tests
sol = Solution()
print(sol.isValid("()"))      # True
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))      # False
print(sol.isValid("([)]"))    # False
print(sol.isValid("{[]}"))    # True
print(sol.isValid("]"))       # False