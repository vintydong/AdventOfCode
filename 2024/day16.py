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
        if (dx, dy) == facing:
            if (-1 < x + dx < n and -1 < y + dy < m) and grid[y+dy][x+dx] != '#' :
                moves.append(((x+dx,y+dy), (dx,dy), 1))
        else:
            moves.append(((x,y), (dx,dy), 1000))
    return moves

def dijkstras(grid, start, end):
    from heapq import heappop, heappush
    seen = {start: 0}
    predecessors = {}
    facing = (1,0)
    queue = [(0, start, facing)]
    while len(queue):
        cost, node, facing = heappop(queue)

        if node == end:
            break

        moves = get_moves(grid, node, facing)
        for next_node, next_dir, weight in moves:
            if (next_node, next_dir) not in seen or cost + weight < seen[(next_node, next_dir)]:
                seen[(next_node, next_dir)] = cost + weight
                predecessors[(next_node, next_dir)] = {(node, facing)}
                heappush(queue, (cost + weight, next_node, next_dir))
            elif cost + weight == seen[(next_node, next_dir)]:
                predecessors[(next_node, next_dir)].add((node, facing))
            else:
                continue
    
    best_path_tiles = set()
    queue = [(node, facing)]
    while len(queue) > 0:
        state = queue.pop()
        if state[0] == start:
            continue
        best_path_tiles.add(state)
        queue.extend(predecessors.get(state, []))
    
    best_path_tiles = set([state[0] for state in best_path_tiles])
    return cost, len(best_path_tiles) + 1

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
    cost, _ = dijkstras(data, start, end)
    # print_disjkstras(data, seen)
    return cost

def part2(data):
    """Solve part 2."""
    start, end = get_start_end(data, s="S", e="E")
    _, num_tiles = dijkstras(data, start, end)

    return num_tiles

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