class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def isOpening(c: str):
            return c == '{' or c == '[' or c == '('

        def getOpening(c: str) -> str:
            match c:
                case '}':
                    return '{'
                case ']':
                    return '['
                case ')':
                    return '('

            return ''

        for c in s:
            if isOpening(c):
                stack.append(c)
                continue

            openParan = getOpening(c)

            if openParan != stack[-1]:
                return False

            stack.pop()

        return len(stack) == 0
