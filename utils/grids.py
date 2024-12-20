from collections import deque

def in_bounds(grid, pos):
    '''Returns whether (x,y) is in bounds for an image-like grid'''
    x, y = pos
    m, n = len(grid), len(grid[0])
    return -1 < x < n and -1 < y < m

def print_grid(grid):
    for row in grid:
        print(''.join(['|'] + [c for c in row] + ['|']))

def bfs_grid(grid, start, end, get_neighbors):
    """
    BFS on a grid returning cost, previous, and visited nodes
    :param grid: 2D image-like grid with x columns and y rows
    :param start: (x,y) for cell at grid[y][x]
    :param end: (x,y) for cell at grid[y][x]
    :param get_neighbors: function(grid, pos) -> list of valid neighbors
    """

    queue = deque([(0, start, start)])
    visited = set()
    previous = {}
    while queue:
        cost, node, prev = queue.popleft()

        if node == end:
            previous[node] = prev
            visited.add(node)
            return cost, previous, visited
        
        if node in visited:
            continue

        previous[node] = prev
        visited.add(node)

        neighbors = get_neighbors(grid, node)
        for n in neighbors:
            queue.append((cost + 1, n, node))

    # raise RuntimeError("No path to end")
    return -1, None, None 