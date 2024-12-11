# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def get_adjacent_pos(data, i, j):
    rows, cols = len(data), len(data[0])
    diffs = [(-1,0),(0,1),(1,0),(0,-1)]
    positions = []
    for dx, dy in diffs:
        if -1 < i + dx < rows and -1 < j + dy < cols:
            positions.append((i+dx, j+dy))
    return positions

def search(data, i, j, unique_paths=False):
    '''Return # of 9s reachable from data[i][j]'''
    queue = [(i,j)]
    count = 0
    reached = set()
    while queue:
        x,y = queue.pop(0)
        if data[x][y] == '9' and (unique_paths or (x,y) not in reached):
            count += 1
            reached.add((x,y))
            continue
        adjacents = get_adjacent_pos(data, x, y)
        for xx,yy in adjacents:
            if data[xx][yy] == str(int(data[x][y]) + 1):
                queue.append((xx,yy))
    return count

def part1(data):
    """Solve part 1."""
    total = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == '0':
                count = search(data, i, j)
                # print("Checking trailblazer at", (i,j), ": ", count)
                total += count
    return total

def part2(data):
    """Solve part 2."""
    total = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == '0':
                count = search(data, i, j, unique_paths=True)
                # print("Checking trailblazer at", (i,j), ": ", count)
                total += count
    return total

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