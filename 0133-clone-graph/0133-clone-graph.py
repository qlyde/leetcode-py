"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        m = {}

        q = deque()
        q.append(node)
        visited = set()
        while q:
            n = q.popleft()

            if n.val not in visited:
                m[n] = Node(n.val)
                visited.add(n.val)
                for neighbour in n.neighbors:
                    q.append(neighbour)

        for old in m:
            m[old].neighbors.extend([m[neighbour] for neighbour in old.neighbors])

        return m[node]
