# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def get_col_heights(grid):
    assert len(grid) == 7 and len(grid[0]) == 5

    col_heights = [0] * 5
    for col in range(5):
        height = 0
        for row in range(1,6):
            if grid[row][col] == '#':
                height += 1
        col_heights[col] = height
    return col_heights
                
def parse(puzzle_input):
    """Parse puzzle"""
    key_or_locks = puzzle_input.split('\n\n')
    keys = set()
    locks = set()
    for grid in key_or_locks:
        grid = grid.strip()
        if grid.split('\n')[0][0] == '.':
            keys.add(tuple(get_col_heights(grid.split('\n'))))
        else:
            locks.add(tuple(get_col_heights(grid.split('\n'))))
    return keys, locks

def part1(data):
    """Solve part 1."""
    keys, locks = data
    print(data)
    count = 0
    for k in keys:
        for l in locks:
            col_sum = [k[i] + l[i] for i in range(5)]
            if all([s <= 5 for s in col_sum]):
                count += 1
    return count

def part2(data):
    """Solve part 2."""

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