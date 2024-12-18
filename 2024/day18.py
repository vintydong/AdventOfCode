# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
from collections import deque
import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse puzzle"""
    lines = puzzle_input.split('\n')
    lines = map(lambda line: list(map(int, re.findall(r'(\d+)', line))), lines)
    SIZE = 71
    return [['.' for _ in range(SIZE)] for _ in range(SIZE)], list(lines)

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
    queue = deque([(0, start)])
    visited = set()
    while queue:
        cost, node = queue.popleft()

        if node == end:
            return cost
        
        if node in visited:
            continue

        neighbors = get_neighbors(grid, node)
        for n in neighbors:
            queue.append((cost + 1, n))
        visited.add(node)
    
    return -1

def corrupt_grid(grid, corrupts, i=0, n=1024):
    n = min(n, len(corrupts))
    while i < n:
        x,y = corrupts[i]
        grid[y][x] = '#'
        i += 1

def print_grid(grid):
    for row in grid:
        print(''.join(['|'] + [c for c in row] + ['|']))

def part1(data):
    """Solve part 1."""
    grid, corrupts = data
    grid = [[c for c in row] for row in grid]
    corrupt_grid(grid, corrupts)
    print_grid(grid)
    return bfs(grid, (0,0), (70,70))


def part2(data):
    """Solve part 2."""
    # binary search for first bit that cuts off end
    grid, corrupts = data
    
    # double corrupt #s until no sol
    i = 0
    n = 1024
    temp_grid = [[c for c in row] for row in grid]
    while True:
        corrupt_grid(temp_grid, corrupts, i=i, n=n)
        if bfs(temp_grid, (0,0), (70,70)) == -1:
            break
        i = n
        n = n * 2
    
    # search between (i,n)
    left = i
    right = n
    while left < right:
        mid = (left + right) // 2
        temp_grid = [[c for c in row] for row in grid]
        corrupt_grid(temp_grid, corrupts, i=0, n=mid)
        if bfs(temp_grid, (0,0), (70,70)) == -1:
            right = mid - 1
        else:
            left = mid + 1
    return str(corrupts[mid])



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