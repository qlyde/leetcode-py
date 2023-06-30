class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "(":
                stack.append(")")
            elif p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            else:
                if not stack:
                    return False

                top = stack.pop()
                if top != p:
                    return False
        return not stack
            