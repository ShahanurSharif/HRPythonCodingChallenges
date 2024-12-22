def bfs(edges, root):
    visited = []
    queue = []
    visited.append(root)
    queue.append(root)

    while queue:
        m = queue.pop(0)
        for node in edges:
            for neighbor in node:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

    print(visited)

if __name__ == "__main__":
    edges = {
        0: [1, 2, 3],
        1: [2, 5, 6],
        2: [3, 5, 8],
        3: [6, 7, 8]
    }

    bfs(edges, 0)