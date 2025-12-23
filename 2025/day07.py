import pathlib
import sys

'''
Part 1: Every beam is an index, when it splits, replace with its neighbors
Part 2: Use DP, store the number of beams (different paths) at each index at the current row
'''

def parse(puzzle_input):
    """Parse puzzle"""
    grid = puzzle_input.split('\n')
    col = grid[0].index('S')
    return (0, col), grid

def part1(data):
    """Solve part 1."""
    start, grid = data
    beams = set()
    beams.add(start[1])
    splits = 0

    for i in range(1, len(grid)):
        new_beams = set()
        row = grid[i]
        for n in beams:
            if row[n] == "^":
                new_beams.add(n-1)
                new_beams.add(n+1)
                splits += 1
            else:
                new_beams.add(n)
        beams = new_beams
    
    return splits

def part2(data):
    """Solve part 2."""
    start, grid = data

    beams = [0] * len(grid[0])
    beams[start[1]] = 1

    for i in range(1, len(grid)):
        row = grid[i]
        new_beams = [0] * len(beams) 
        for j in range(len(beams)):
            if row[j] == "^":
                new_beams[j-1] += beams[j]
                new_beams[j+1] += beams[j]
            else:
                new_beams[j] += beams[j]
        beams = new_beams

    return sum(beams)

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