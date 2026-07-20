class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }
        for c in s:
            if stack and (c == '}' or c == ']' or c == ')') and match[c] == stack[-1]:
                stack.pop()
            elif c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                return False
        return True if not stack else False