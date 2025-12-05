import pathlib
import sys

'''
Part 1: Check for end results of 0 (mod 100)
Part 2: Check for passing 0 (mod 100)

Needed to account for double counting when moving left from 0
'''

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def part1(data):
    """Solve part 1."""
    curr = 50
    count = 0
    dirs = {'L': -1, 'R': 1}
    for line in data:
        curr += dirs[line[0]] * int(line[1:])
        if curr % 100 == 0:
            count += 1
    return count

def part2(data):
    """Solve part 2."""
    curr = 50
    count = 0
    dirs = {'L': -1, 'R': 1}
    for line in data:
        prev = curr
        direction = dirs[line[0]]
        curr += direction * int(line[1:])

        # Want round to 0 division instead of round down (to -infinity)
        # curr//100 -> floor after division
        # int(curr/100) -> truncate after division
        # // works for positive numbers
        if direction == -1:
            count += abs(int(curr / 100)) + (1 if prev != 0 and curr <= 0 else 0)
        elif direction == 1:
            count += curr // 100
        curr = curr % 100
    return count

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