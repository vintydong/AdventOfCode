# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
from collections import deque
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return [[c for c in line] for line in puzzle_input.split('\n')]

def get_start_end(grid, s, e):
    start, end = None, None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == s:
                start = (c,r)
            if cell == e:
                end = (c,r)
            
            if start and end:
                break
        else:
            continue
        break
    return start, end

def get_moves(grid, cell, facing):
    '''Get moves at cell facing a direction'''
    dirs = [(1,0),(0,-1),(-1,0),(0,1)]
    x,y = cell
    index = dirs.index(facing)
    
    m, n = len(grid), len(grid[0])
    avail = [dirs[index], dirs[(index-1) % 4], dirs[(index+1) % 4]]
    moves = []
    for dx, dy in avail:
        if (-1 < x + dx < n and -1 < y + dy < m) and grid[y+dy][x+dx] != '#' :
            moves.append((x+dx,y+dy))
    return moves

def dijkstras(grid, start):
    seen = {}
    predecessors = {}
    facing = (1,0)
    queue = deque([(start, 0, facing, None)])
    while len(queue):
        node, cost, facing, prev = queue.popleft()
        if node not in seen or cost < seen[node]:
            seen[node] = cost
            predecessors[node] = set([prev] if prev is not None else [])
        elif cost == seen[node]:
            predecessors[node].add(prev)
        else:
            continue
        moves = get_moves(grid, node, facing)
        for m in moves:
            if m == tuple((node[i] + facing[i] for i in range(2))):
                queue.append((m, cost+1, facing, node))
            else:
                queue.append((m, cost+1001, tuple((m[i] - node[i] for i in range(2))), node))
    return seen, predecessors

def print_disjkstras(grid, seen):
    grid = [[c for c in line] for line in grid]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '.':
                grid[r][c] = seen.get((c,r), -1)
    [print('|' + ','.join([str(c).rjust(5, ' ') for c in row]) + '|') for row in grid]

def print_best_tiles(grid, best_tiles):
    grid = [[c for c in line] for line in grid]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if (c,r) in best_tiles:
                grid[r][c] = 'O'
    [print('|' + ','.join([str(c).rjust(1, ' ') for c in row]) + '|') for row in grid]

def part1(data):
    """Solve part 1."""
    start, end = get_start_end(data, s="S", e="E")
    seen, predecessors = dijkstras(data, start)
    print_disjkstras(data, seen)
    return seen[end]

def part2(data):
    """Solve part 2."""
    start, end = get_start_end(data, s="S", e="E")
    seen, predecessors = dijkstras(data, start)

    best_path_tiles = set()
    queue = [end]
    while len(queue) > 0:
        node = queue.pop()
        best_path_tiles.add(node)
        queue.extend(predecessors.get(node, []))
    print_best_tiles(data, best_path_tiles)
    return len(best_path_tiles)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    path = 'input.txt'
    if len(sys.argv) > 1 and sys.argv[1]:
        path = 'input2.txt'

    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))