from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
room_list = []
visited = set()
########################
# While length of visited rooms is less than length of len(list(world.rooms))

# 1) Add current room to list
# 2) Get from back of list
# 3) Check to see if it is in visited
#   3a) If not, add it with directions to rooms 
# 4) Check to see if there are unexplored rooms in the room (using key in dictionary)
#   4a) If there are, add them to list of unexplored rooms 
# 5) Remove last element from list (already explored)
# 6) Go through neighbors of room
#   6a) Compare each neighbor id to the room id in list, and add direction to the traversal list.

room_list += [player.current_room.id]
while len(list(visited)) < len(list(world.rooms)):

    # Get the last element of the room_list
    cur_room = room_list[-1]
    # Add to visited
    visited.add(cur_room)

    # Instantiate queue to hold rooms
    room_queue = Queue()
    
    # Find neighbors of room
    neighbors = room_graph[cur_room][1]
    # For each value in the key of this dictionary
    for r in neighbors.values():
        # If they are not in visited
        if r not in visited:
            # Add them to the room queue
            room_queue.enqueue(r)
    
    # If the queue is greater than 0
    if room_queue.size() > 0:
        # Remove the room from the queue
        new_room = room_queue.dequeue()
        # Add it to our room list
        room_list.append(new_room)
    else:
        # Remove visited room from room list (prevents infinite loop)
        room_list.pop()
        # print(room_list)

    # For each room in neighbors
    for r in neighbors.items():
        # If the room id in the room element is the last element in our room list
        print(r)
        if r[1] == room_list[-1]:
            # Append the direction from the room element
            traversal_path.append(r[0])




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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
