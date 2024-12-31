arr = [1, 2, 3, 4]
marked = [False]*len(arr)

def visit(node):
    pass


def neighbors(node):
    pass


def Dfs(arr, node):
    visit(node)
    marked[node] = True
    for i in neighbors(node):
        if not marked[i]:
            Dfs(arr, i)