"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        base = None
        if not node:
            return base
        stack = []
        stack.append(node)

        while stack:
            curr = stack.pop()
            if visited.get(curr) == None:
                visited[curr] = Node(curr.val)
            if not base:
                base = visited[curr]

            for neighbor in curr.neighbors:
                if visited.get(neighbor) == None:
                    visited[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        
        return base
