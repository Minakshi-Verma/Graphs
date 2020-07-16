
from util import Queue

#Tim's solution
# Understood

# Plan
## Graphs Problem Solving
### Translate the problem
#### Nodes: people
#### Edges: when a child has a parent

### build our graph, or just define get_neighors
#### 

### Choose algorithm
#### Either BFS or DFS
#### DFS
##### How would we know if DFS happened to be faster?

# import deque from collections


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighors(self, vertex):
        return self.vertices[vertex]

## Build a path like we did in search
## But we don't know when to stop until we've seen everyone
def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = [starting_node]
    aged_one = -1   # aged_ones are the earliest ancestor

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        # if path is longer, or path is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)

    return aged_one
#________________________________________________________________
               #ALTERNATE SOLUTION

# def earliest_ancestor(ancestors, starting_node):
#     # BFS
#     # parent and children make the nodes
#     # relationship between parent and child make the edge

#     # make a stack
#     q = Queue()
#     #add the node to the path( only one node in the starting)
#     path = [starting_node]

#     #add the path to the queue
#     q.enqueue(path)

#     # # make a set to track if we've visited there
#     # visited = set()

#     # while the queue isn't empty
#     while q.size()>0:

#         ##pop off whatever's at the front of stack, 
#         #this is our current node        
#         current_path = q.dequeue() 

#         # current_node = current_path[-1]
#         # ##if we haven't visisted this node yet

#         # if current_node not in visited:
#         #     #mark as visited
#         #     visited.add(current_node)
#         #     print(visited)

#         new_path = []     
#         changed = False

#         # get begin node of path
#         for node in current_path:
#             # loop through ancestors for parents
#             for ancestor in ancestors:
#                 # # a tuple(parent, child)
#                 # look into each ancestor parent with start_node as child
#                 if ancestor[1] == node: #that mean there is child node
#                     # print(ancestor[1]) 
#                     new_path.append(ancestor[0]) #append the parent 
#                     changed = True
#                     q.enqueue(new_path)
# # 
#         if changed is False:
#             if current_path[0] == starting_node:
#                 # print(current_path[0])                
#                 return -1

#             else:                
#                 return current_path[0]

      

