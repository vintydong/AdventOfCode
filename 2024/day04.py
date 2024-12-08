import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def check_diagonals(data, i, j):
    diffs = [(-1,-1),(-1,1),(1,-1),(1,1)]
    s = 0
    for dx,dy in diffs:
        indices = [(i+k*dx, j+k*dy) for k in range(4)]
        # check last index is in-bounds
        if 0 <= indices[-1][0] < len(data) and 0 <= indices[-1][1] < len(data[i]):
            substring = "".join([data[x][y] for x,y in indices])
            if substring == "XMAS":
                s += 1
    return s


def check_horizontals(data, i, j):
    line = data[i]
    s = 0
    if j >= 3 and line[j-3:j+1] == "SAMX":
        s += 1
    if j < len(line) - 3 and line[j:j+4] == "XMAS":
        s += 1
    return s

def check_verticals(data, i, j):
    s = 0
    if i >= 3 and "".join([data[i-k][j] for k in range(4)]) == "XMAS":
        s += 1
    if i < len(data) - 3 and "".join([data[i+k][j] for k in range(4)]) == "XMAS":
        s += 1
    return s

def part1(data):
    """Solve part 1."""
    s = 0
    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            char = line[j]
            if char == "X":
                s += check_diagonals(data, i, j) + check_horizontals(data, i, j) + check_verticals(data, i, j)
    return s

def check_mas(data, i, j):
    diffs = [(-1,-1),(-1,1),(1,1),(1,-1)]

    # check in-bounds
    if not(0 < i < len(data)-1 and 0 < j < len(data[i]) - 1):
        return 0

    indices = [(i+x,j+y) for x,y in diffs]
    # indices should contain 2 M 2 S consecutive
    M_counts, S_counts = 0, 0
    consecutive = False
    prev = None
    for x,y in indices:
        char = data[x][y]
        if char == "M": M_counts += 1
        if char == "S": S_counts += 1
        if prev == char: consecutive = True
        prev = char
    if consecutive and M_counts == 2 and S_counts == 2:
        return 1
    return 0

def part2(data):
    """Solve part 2."""
    s = 0
    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            char = line[j]
            if char == "A":
                s += check_mas(data, i, j)
    return s


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = pathlib.Path('input.txt').read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))