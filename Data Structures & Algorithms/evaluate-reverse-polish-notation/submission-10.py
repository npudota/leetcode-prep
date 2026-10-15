class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            
            if t == "+":
                d1, d2 = stack.pop(), stack.pop()
                stack.append(d1 + d2)
            elif t == "-":
                 d1, d2 = stack.pop(), stack.pop()
                 stack.append(d2 - d1)
            elif t == "*":
                 d1, d2 = stack.pop(), stack.pop()
                 stack.append(d2 * d1)
            elif t == "/":
                 d1, d2 = stack.pop(), stack.pop()
                 stack.append(int(d2 / d1))
            else:
                stack.append(int(t))

        return stack[-1]
        
            

        