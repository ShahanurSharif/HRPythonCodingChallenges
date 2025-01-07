arr = [1, 2, 3, 4, 5]
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

def Dfs_Pre(arr, node):
    visit(node)
    marked[node] = True
    for i in neighbors(node):
        if not marked[i]:
            Dfs(arr, i)

def Dfs_Post(arr, node):
    marked[node] = True
    for i in neighbors(node):
        if not marked[i]:
            Dfs_Post(arr, i)
    visit(node)


def DFS_iter(arr, node):
    stack = [node]
    while len(stack)>0:
        node = stack.pop()
        marked[node] = True
        for i in neighbors(node):
            if not marked[i]:
                stack.append(i)