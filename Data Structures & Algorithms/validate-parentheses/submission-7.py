class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackpair = {"]":"[","}":"{",")":"("}
        for i in s:
            if i in stackpair:
                if stack and stack[-1] == stackpair[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False