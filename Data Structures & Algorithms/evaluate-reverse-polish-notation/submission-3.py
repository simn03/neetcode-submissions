class Solution:


    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            match t:
                case '-':
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    res = arg1 - arg2
                    stack.append(res)
                case '+':
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    res = arg1 + arg2
                    stack.append(res)
                case '*':
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    res = arg1 * arg2
                    stack.append(res)
                case '/':
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    res = arg1 / arg2
                    res = math.floor(res) if res > 0 else math.ceil(res)
                    stack.append(res)
                case _:
                    stack.append(int(t))

        return stack.pop()
                    