# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
from collections import deque
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return [[c for c in line] for line in puzzle_input.split('\n')]

def get_start_end(grid):
    start, end = None, None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (c,r)
            if cell == 'E':
                end = (c,r)
            
            if start and end:
                break
        else:
            continue
        break
    return start, end

def get_neighbors(grid, pos):
    x, y = pos
    m, n = len(grid), len(grid[0])
    dirs = [(1,0),(0,-1),(-1,0),(0,1)]
    neighbors = []
    for dx, dy in dirs: 
        if -1 < x + dx < n and -1 < y + dy < m and grid[y+dy][x+dx] != '#':
            neighbors.append((x+dx, y+dy))
    return neighbors

def bfs(grid, start, end):
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

    raise RuntimeError("No path to end")

def part1(data):
    """Solve part 1."""
    start, end = get_start_end(data)
    cost, previous, visited = bfs(data, start, end)
    
    path = []
    node = end
    while True:
        path.append(node)
        if node == start:
            break
        node = previous[node]
    path.reverse()

    node_indices = {node: i for i,node in enumerate(path)}

    # Follow path and try to go through a wall to another tile on path
    # Time is only saved when going straight through a wall
    cheats_used = {}
    dirs = [(1,0),(0,-1),(-1,0),(0,1)]
    m, n = len(data), len(data[0])
    count = 0
    for node in path:
        x, y = node
        for dx, dy in dirs:
            wall_node = data[y+dy][x+dx]
            next_pos = (x+dx+dx, y+dy+dy)
            
            if -1 < x + dx < n and -1 < y + dy < m and wall_node == '#':
                if next_pos in visited:
                    # print(f"Cheat through wall {wall_pos} from {node} to {next_pos}")
                    index_diff = node_indices[next_pos] - node_indices[node]
                    # print(f"Saved {index_diff - 2}")
                    if index_diff > 2:
                        cheats_used[node] = index_diff - 2
                        # print("Saved", index_diff - 2)
                        if index_diff - 2 >= 100:
                            count += 1
    seconds_saved = {}
    for k in cheats_used:
        s = cheats_used[k]
        seconds_saved[s] = seconds_saved.get(s, 0) + 1
    return count

def in_bounds(grid, pos):
    x, y = pos
    m, n = len(grid), len(grid[0])
    return -1 < x < n and -1 < y < m

def get_cheat_end_tiles(grid, pos):
    '''Get tiles within manhattan distance of n'''
    tiles = []
    # Move 1 to 20 tiles in same row
    for i in range(1, 21):
        left = (pos[0] - i, pos[1])
        right = (pos[0] + i, pos[1])
        if in_bounds(grid, left) and grid[left[1]][left[0]] != '#':
            tiles.append(left)
        if in_bounds(grid, right) and grid[right[1]][right[0]] != '#':
            tiles.append(right)
    # Move up/down i squares and 20-i left/right
    for i in range(1, 21):
        # up
        tile = (pos[0], pos[1] + i)
        for j in range(0, 20-i+1):
            x, y = tile[0] + j, tile[1]
            if in_bounds(grid, (x,y)) and grid[y][x] != '#':
                tiles.append((x,y))

            x, y = tile[0] - j, tile[1]
            if in_bounds(grid, (x,y)) and grid[y][x] != '#':
                tiles.append((x,y))
        # down
        tile = (pos[0], pos[1] - i)
        for j in range(0, 20-i+1):
            x, y = tile[0] - j, tile[1]
            if in_bounds(grid, (x,y)) and grid[y][x] != '#':
                tiles.append((x,y))

            x, y = tile[0] + j, tile[1]
            if in_bounds(grid, (x,y)) and grid[y][x] != '#':
                tiles.append((x,y))
    
    return tiles

def print_grid(grid):
    for row in grid:
        print(''.join(['|'] + [c for c in row] + ['|']))

def part2(data):
    """Solve part 2."""
    start, end = get_start_end(data)
    cost, previous, visited = bfs(data, start, end)
    
    path = []
    node = end
    while True:
        path.append(node)
        if node == start:
            break
        node = previous[node]
    path.reverse()

    node_indices = {node: i for i,node in enumerate(path)}

    TEST_TILES = get_cheat_end_tiles(data, start)
    for tile in TEST_TILES:
        data[tile[1]][tile[0]] = 'T'

    # Follow path and try to go to any tile within 20 steps of the current tile
    # Only count destination further along the path
    cheats_used = {}
    for node in path:
        x, y = node

        for tile in get_cheat_end_tiles(data, node):
            if tile in visited and node_indices[tile] > node_indices[node]:
                # Skip recomputing cheats with same start and end
                if (node, tile) in cheats_used:
                    continue

                index_diff = node_indices[tile] - node_indices[node]
                time_saved = index_diff - sum([abs(node[i] - tile[i]) for i in range(2)])
                cheats_used[(node, tile)] = time_saved
    count = 0
    seconds_saved = {}
    for k in cheats_used:
        s = cheats_used[k]
        if s <= 0:
            continue
        seconds_saved[s] = seconds_saved.get(s, 0) + 1
    
    count = 0
    for k in seconds_saved:
        if k >= 100:
            count += seconds_saved[k]
    return count

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    # solution1 = part1(data)
    solution2 = part2(data)

    return 0, solution2

if __name__ == "__main__":
    path = 'input.txt'
    if len(sys.argv) > 1 and sys.argv[1]:
        path = 'input2.txt'

    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))