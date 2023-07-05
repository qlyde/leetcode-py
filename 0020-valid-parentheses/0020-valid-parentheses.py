class Solution:
    def isValid(self, s: str) -> bool:
        m = {")": "(", "}": "{", "]": "["}
        stack = []
        for p in s:
            if p not in m:
                stack.append(p)
            else:
                if not stack or stack[-1] != m[p]:
                    return False
                stack.pop()
        return not stack
            