
from util import Queue



def earliest_ancestor(ancestors, starting_node):
    # BFS
    # parent and children make the nodes
    # relationship between parent and child make the edge

    # make a stack
    q = Queue()
    #add the node to the path( only one node in the starting)
    path = [starting_node]

    #add the path to the queue
    q.enqueue(path)

    # make a set to track if we've visited there
    visited = set()

    # while the queue isn't empty
    while q.size():
        ##pop off whatever's at the front of stack, this is our current node
        current_node = q.dequeue()
        ##if we haven't visisted this node yet
        if current_node not in visited:
            #mark as visisted
            visited.add(current_node)

            #get the children--neighbors

