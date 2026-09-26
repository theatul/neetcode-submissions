"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.existingNode = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return 
        
        # Copy existing node
        temp = Node(node.val, [])
        self.existingNode[node.val] =  temp
        # Copy children recursively
        for n in node.neighbors:
            if n.val in self.existingNode:
                child = self.existingNode[n.val]
            else:
                child = self.cloneGraph(n)
            temp.neighbors.append(child)
        
        return temp