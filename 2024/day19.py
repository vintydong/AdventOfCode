# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    patterns, towels = puzzle_input.split('\n\n')
    patterns = patterns.split(', ')
    patterns.sort()
    towels = towels.split('\n')
    return patterns, towels

def make_towel(towel, patterns, cache):
    if towel == '':
        return 1
    
    res = []

    if towel in cache:
        return cache[towel]
    
    # # binary search for first char
    # left = 0 
    # right = len(patterns)
    # while left < right:
    #     mid = (left + right) // 2
    #     if patterns[mid][:2] >= towel[:2]:
    #         right = mid - 1
    #     elif patterns[mid][:2] < towel[:2]:
    #         left = mid + 1
    
    for p in patterns:
        if towel.startswith(p):
            res.append(make_towel(towel[len(p):], patterns, cache))
    cache[towel] = sum(res)
    return sum(res)

def part1(data):
    """Solve part 1."""
    patterns, towels = data
    count = 0
    for towel in towels:
        count += 1 if make_towel(towel, patterns, {}) > 0 else 0
    return count

def part2(data):
    """Solve part 2."""
    patterns, towels = data
    count = 0
    for i, towel in enumerate(towels):
        print("Iteration", i)
        count += make_towel(towel, patterns, {})

    return count

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    # solution1 = part1(data)
    solution2 = part2(data)

    return 0, solution2

if __name__ == "__main__":
    path = 'input.txt'
    if len(sys.argv) > 1 and sys.argv[1]:
        path = 'input2.txt'

    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))