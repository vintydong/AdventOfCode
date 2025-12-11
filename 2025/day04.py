import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from utils.grids import in_bounds

'''
Part 1: Iterate over grid and count neighbors
Part 2: Repeatedly remove rolls with <4 neighbors until stable
'''

def parse(puzzle_input):
    """Parse puzzle"""
    return [[c for c in line] for line in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1."""
    grid = data
    r,c = len(grid), len(grid[0])

    count = 0

    for x in range(r):
        for y in range(c):
            if grid[x][y] != '@':
                continue

            dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            neighbor_rolls = 0
            for dx,dy in dirs:
                nx, ny = (x+dx, y+dy)
                if in_bounds(grid, (nx,ny)) and grid[nx][ny] == '@':
                    neighbor_rolls += 1
            if neighbor_rolls < 4:
                count += 1
    return count

def part2(data):
    """Solve part 2."""
    grid = data
    r,c = len(grid), len(grid[0])

    removed_count = 0

    while True:
        removable = []
        for x in range(r):
            for y in range(c):
                if grid[x][y] != '@':
                    continue

                dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
                neighbor_rolls = 0
                for dx,dy in dirs:
                    nx, ny = (x+dx, y+dy)
                    if in_bounds(grid, (nx,ny)) and grid[nx][ny] == '@':
                        neighbor_rolls += 1
                if neighbor_rolls < 4:
                    removable.append((x,y))
        if not len(removable):
            break
        for x,y in removable:
            grid[x][y] = '.'
        removed_count += len(removable)

    return removed_count

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