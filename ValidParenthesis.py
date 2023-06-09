def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "}": "{", "]": "["}
    if len(s) % 2 != 0:
        return False
    else:
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False