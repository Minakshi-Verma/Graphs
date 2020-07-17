from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map

# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# store the directions that has been traveled
reverse_dir= {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

#Keep track of path traversed to visit rooms
traversal_path = []

#Keep track of backtracked path while visiting rooms
reversed_path= []

# Keep track of all the rooms visited
rooms= {}
 # Add the the 1st room--index[0]  to  rooms 
 # check for available direction to added room
rooms[0]= player.current_room.get_exits()
# print(rooms)

 # Check if all the rooms are added or not
while len(rooms)< len(room_graph):
    # print(rooms[player.current_room.id])
    # print(player.current_room.id)
    # if room is not visited 
    if (player.current_room.id) not in rooms: 
        # Add exit from current rooms other rooms     
        rooms[player.current_room.id]= player.current_room.get_exits()
    # print(player.current_room.id)
# last_dir = reversed_path[-1]
# print(last_dir)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")




