# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        queue = []
        self.dict = {}
        cloneNode = UndirectedGraphNode(node.label)
        queue.append(node)
        self.dict[node] = cloneNode
        while len(queue) != 0:
            curNode = queue[0]
            del queue[0]
            curCloneNode = self.getOrCreate(curNode)
            for eachNode in curNode.neighbors:
                if self.dict.has_key(eachNode):
                    curCloneNode.neighbors.append(self.dict[eachNode])
                else:
                    curCloneNode.neighbors.append(self.getOrCreate(eachNode))
                    queue.append(eachNode)
        return cloneNode
    def getOrCreate(self, node):
        if self.dict.has_key(node):
            return self.dict[node]
        else:
            cloneNode = UndirectedGraphNode(node.label)
            self.dict[node] = cloneNode
            return cloneNode
