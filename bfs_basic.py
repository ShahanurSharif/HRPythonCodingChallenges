edges = {
    0: [1, 2, 3],
    1: [2, 5, 6],
    2: [3, 5, 6],
    3: [6, 7, 8]
}

visited = []
queue = []

def bfs(edges, root):
    visited.append(root)
    queue.append(root)

    while queue:
        m = queue.pop(0)
        # print(m, end = " ")
        for neighbor in edges[m]:
            print('edges', neighbor, [m])
            # if neighbor not in visited:




if __name__ == "__main__":
    bfs(edges, 0)