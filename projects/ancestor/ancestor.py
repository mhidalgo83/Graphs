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


def get_ancestors(node, ancestors):
    ancestor_list = []
    for a in ancestors:
        if node == a[1]:
            ancestor_list.append(a[0])
    return ancestor_list


def earliest_ancestor(ancestors, starting_node):
    a_list = []
    q = Queue()
    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        for a in get_ancestors(v, ancestors):
            new_path = path + [a]
            if len(a_list) == 0:
                a_list.append(new_path)
            if len(new_path) > len(a_list[0]):
                a_list[0] = new_path
            if len(new_path) == len(a_list[0]) and new_path != a_list[0]:
                a_list.append(new_path)        
            q.enqueue(new_path)
    if len(a_list) == 0:
        return -1
    else:
        if len(a_list) == 2:
            if len(a_list[0]) == len(a_list[1]):
                if a_list[0][-1] < a_list[1][-1]:
                    return a_list[0][-1]
                return a_list[1][-1]
        return a_list[0][-1]
    # elif len(a_list) == 1:
    #     return a_list[0][-1]
    # elif len(a_list) == 2:
    #     if a_list[0][-1] < a_list[1][-1]:
    #         return a_list[0][-1]
    #     else:
    #         return a_list[1][-1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (11, 8), (8, 9), (4, 8), (10, 1)]

print(earliest_ancestor(ancestors, 9))
# print(get_ancestors(3, ancestors))
