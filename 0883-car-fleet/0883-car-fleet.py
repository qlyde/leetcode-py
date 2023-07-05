class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pss = [(p, s) for p, s in zip(position, speed)]
        pss.sort()
        for ps in pss[::-1]:
            t = (target - ps[0]) / ps[1]
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)

# pss[::-1] -> (10,2), (8,4), (5,1), (3,3), (0,1)
#         t ->      1,     1,     7,     3,    12
#     stack ->      1,     _,     7,     _,    12
#       ret -> 3
