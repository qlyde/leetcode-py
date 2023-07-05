class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ( allowed if: opened < n
        # ) allowed if: closed < opened
        ret = []
        self.backtrack(n, ret=ret)
        return ret

    def backtrack(self, n, opened=0, closed=0, ps=[], ret=[]):
        if opened == closed == n:
            ret.append(''.join(ps))

        if opened < n:
            self.backtrack(n, opened + 1, closed, ps + ["("], ret)
        if closed < opened:
            self.backtrack(n, opened, closed + 1, ps + [")"], ret)
