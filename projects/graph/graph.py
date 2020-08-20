"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
#__________________________________________________________________

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
#__________________________________________________________________

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
#__________________________________________________________________

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
   
#__________________________________________________________________

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        # UPER STEPS

        #1-make a queue
        q = Queue()

        #2- enqueue our starting node
        q.enqueue(starting_vertex)

        #3- make a set to track if we've been here before 
        visited = set()

        #4-while our queue isn't empty
        while q.size() > 0:

        ##  dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
            ##if we haven't visited this node yet,
            if current_node not in visited:
                ### mark as visited
                visited.add(current_node)
                #print all the vertices
                print(current_node)
            
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors,
                for neighbor in neighbors:
                    #### add to queue
                    q.enqueue(neighbor) 

#_____________________________________________________________________        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
           
        # UPER STEPS
        #1-make a stack
        s = Stack()

        #2- push our starting node
        s.push(starting_vertex)

        #3- make a set to track if we've been here before 
        visited = set()

        #4-while our stack isn't empty
        while s.size() > 0:

        ##  pop off whatever's at the front of our line, this is our current_node
            current_node = s.pop()
            ##if we haven't visited this node yet,
            if current_node not in visited:
                ### mark as visited
                visited.add(current_node)
                #print all the vertices
                print(current_node)
            
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors,
                for neighbor in neighbors:
                    #### add to the stack
                    s.push(neighbor)

#_____________________________________________________________________
     
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
​
        This should be done using recursion.
        """
        # mark this vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
        ## if it's not visited
            if neighbor not in visited:
        ### recurse on the neighbor
                self.dft_recursive(neighbor, visited)   

             #-------------------------------------#
                         #ALTERNATIVE
    # def dft_recursive(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
       
    #     #Keep track of visited outside of recursive call
    #     visited = set()

    #     def dft_inner(vertex):
    #         if vertex in visited:
    #             return
    #         else:
    #             visited.add(vertex)
    #         print(vertex)

    #         neighbors = self.get_neighbors(vertex)

    #         for neighbor in neighbors:
    #             dft_inner(neighbor)

    #     dft_inner(starting_vertex)

#_______________________________________________________________________

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # make a queue
        q = Queue()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        # while queue isn't empty
        while q.size() > 0:
        ## dequeue the path at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]

        ### if this node is our target node
            if current_node == destination_vertex:
        #### return it!! return TRUE
                return current_path

        ### if not visited
            if current_node not in visited:
        #### mark as visited
                visited.add(current_node)
        #### get its neighbors
                neighbors = self.get_neighbors(current_node)
        #### for each neighbor
                for neighbor in neighbors:
                    ## copy path so we don't mutate the original path for different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                ##### add to our queue
                    q.enqueue(path_copy)


                #------------------------------------------#
                               # ALTERNATE

    # def bfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing the shortest path from
    #     starting_vertex to destination_vertex in
    #     breath-first order.
    #     """
   
    #     # make a queue
    #     q_bft_path = Queue() 

    #     #enqueue the starting node
    #     q_bft_path.enqueue([starting_vertex])

    #     #make a set to track if we've been here before
    #     visited = set()
        
    #     #4-while our queue isn't empty
    #     while q_bft_path.size() > 0:
    #         ##  dequeue whatever's at the front of our line, this is our current_node
    #         cur_node_path = q_bft_path.dequeue()
    #         # get the last node[-1]
    #         last_node = cur_node_path[-1]
            
    #         ##if we haven't visited this node yet
    #         if last_node not in visited:
    #             #mark as visited
    #             visited.add(last_node)
    #             #print all the vertices
    #             print(last_node)
    #         ### get its neighbors
    #         neighbors = self.get_neighbors(last_node)
    #         ### for each of the neighbors,
    #         for neighbor in neighbors:
    #             next_node_path = cur_node_path.copy()
    #             print(type(next_node_path))
    #             next_node_path.append(neighbor)

    #             # check if neighbor is destination node
    #             if neighbor == destination_vertex:
    #                 return next_node_path
    #             #add the next node path to existing one
    #             q_bft_path.enqueue(next_node_path)

#____________________________________________________________________

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
            
        #1-make a stack ( using a placeholder s)
        s = Stack() 

        #2- push our starting node
        s.push([starting_vertex])

        #3- make a set to track if we've been here before 
        visited = set()

        #4-while our stack isn't empty
        while s.size() > 0:
            ##  pop off whatever's at the front of our line, this is our current node
            cur_path = s.pop()
            # get the last node of the path[-1]
            last_node = cur_path[-1]


             #if we haven't visited this node yet,
            if last_node not in visited:
                ### mark as visited
                visited.add(last_node)
                #print all the vertices
                print(last_node)

            ### get its neighbors
            neighbors = self.get_neighbors(last_node)

            ### for each of the neighbors,
            for neighbor in neighbors:
                next_path = cur_path.copy()
                next_path.append(neighbor)

                # check if neighbor is destination node
                if neighbor == destination_vertex:
                    return next_path
                #add the next node path to existing one
                s.push(next_path)

#_____________________________________________________________________
    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        ## mark our node as visited
        visited.add(vertex)

        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)
        
        ## iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result


                 #------------------------------------------#
                               # ALTERNATE

    # def dfs_recursive(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
       
    #     visited = set()

    #     def dft_inner(path):
    #         last_vertex = path[-1]

    #         if last_vertex in visited:
    #             return None
    #         else:
    #             visited.add(last_vertex)

    #         if last_vertex == destination_vertex:
    #             return path

    #         neighbors = self.get_neighbors(last_vertex)
    #         for neighbor in neighbors:
    #             next_path = path.copy()
    #             next_path.append(neighbor)

    #             found = dft_inner(next_path)
    #             if found:
    #                 return found

    #         return None

    #     return dft_inner([starting_vertex])
#______________________________________________________________________

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
