def bfs(edges, root):
    visited = []
    queue = []
    visited.append(root)
    queue.append(root)

    while queue:
        for neighbour in edges[queue]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    edges = {
        0: [1, 2, 3],
        1: [2, 5, 6],
        2: [3, 5, 8],
        3: [6, 7, 8]
    }

    bfs(edges, 0)