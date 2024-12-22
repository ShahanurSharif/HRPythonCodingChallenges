edges = {
    0: [1, 2, 3],
    1: [2, 5, 6],
    2: [3, 5, 6],
    3: [6, 7, 8]
}

def bfs(edges, root):
    visited = []
    queue = []
    visited.append(root)
    queue.append(root)

    while queue:
        m = queue.pop(0)

        print(m, end = " ")
        for neighbor in edges[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                print(visited, queue)




if __name__ == "__main__":
    bfs(edges, 1)