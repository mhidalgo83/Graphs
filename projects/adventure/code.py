def traverse_path(r, p):
    s = Stack()
    s.push(r)
    cur_path = []
    while s.size() > 0:
        room = s.pop()
        if room.id not in visited:
            visited[room.id] = {}
            for d in room.get_exits():
                visited[room.id][d] = "?"
            if visited[room.id][d] == "?":
                player.travel(d)
                s.push(player.current_room)

def in_room(r, p):
    data = Queue ()
    data.enqueue(r)
    prev_room = None
    while data.size() > 0: 
        room = data.dequeue()
        if room.id not in visited:
            visited[room.id] = {}
            for d in room.get_exits():
                visited[room.id][d] = "?"
                # if prev_room is not None:
                #     if traversal_path[-1] == "n":
                #         visited[room.id]["s"] = prev_room.id
                #         visited[prev_room.id]["n"] = room.id
                #     if traversal_path[-1] == "s":
                #         visited[room.id]["n"] = prev_room.id
                #         visited[prev_room.id]["s"] = room.id
                #     if traversal_path[-1] == "w":
                #         visited[room.id]["e"] = prev_room.id
                #         visited[prev_room.id]["w"] = room.id
                #     if traversal_path[-1] == "e":
                #         visited[room.id]["w"] = prev_room.id
                #         visited[prev_room.id]["e"] = room.id
                # print(traversal_path)
                print(visited)   
                print("---------")
                print(list(visited[room.id][d]))
                traverse_path(player.travel(d), player)

                # for u_r in list(visited[room.id][d]):
                #     if u_r == "?":
                #         traverse_path(player.travel(d), player)
                
traverse_path(player.current_room, player)