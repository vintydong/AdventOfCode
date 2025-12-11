import pathlib
import sys

'''
Part 1: Check each ID against each range
Part 2: (merge interval problem) Count unique IDs covered by overlapping ranges
'''

def parse(puzzle_input):
    """Parse puzzle"""
    ranges, ids = puzzle_input.split('\n\n')
    ranges = ranges.split('\n')
    for i,r in enumerate(ranges):
        low, high = ranges[i].split('-')
        ranges[i] = (int(low), int(high))

    ids = [int(id) for id in ids.split('\n')]
    return ranges, ids

def part1(data):
    """Solve part 1."""
    ranges, ids = data
    count = 0
    for id in ids:
        for low, high in ranges:
            if low <= id <= high:
                count += 1
                break
    return count


def part2(data):
    """Solve part 2."""
    ranges, ids = data
    count = 0
    ranges = sorted(ranges)
    curr = ranges[0]
    for r in ranges[1:]:
        low, high = r
        if low > curr[1]: # new non-overlap interval
            count += (curr[1] - curr[0] + 1)
            curr = (low, high)
        elif low >= curr[0] and high >= curr[1]: # overlap interval
            curr = (curr[0], high)
        elif low >= curr[0] and high <= curr[1]: # contained interval
            continue
    count += (curr[1] - curr[0] + 1)
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