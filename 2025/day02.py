import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split(',')

def part1(data):
    """Solve part 1."""
    total = 0
    for id_range in data:
        l,r = id_range.split('-')
        l,r = int(l), int(r)

        i = 1
        while int(str(i) * 2) < l:
            i += 1

        while int(str(i) * 2) <= r:
            total += int(str(i) * 2)
            i += 1
    return total

def repeat(x, n):
    '''Repeat the digits of x n times i.e. (12, 3) -> 121212'''
    i = x
    digits = 0
    while i > 0:
        i //= 10
        digits += 1
    i = x
    while n > 1:
        i = (i * (10 ** digits)) + x
        n -= 1
    return i

def part2(data):
    """Solve part 2."""
    total = 0
    num_set = set()
    for id_range in data:
        l,r = id_range.split('-')
        l,r = int(l), int(r)

        # repeat (i) n times
        # iterate over n, starting from 2 (part 1)
        # iterate over i, same as part 1
        i = 1
        n = 2
        while repeat(i,n) < r: # check if greater than range
            # part 1 but for a given n instead of n=2
            while repeat(i,n) < l:
                i += 1

            while repeat(i,n) <= r:
                if repeat(i,n) not in num_set:
                    total += repeat(i,n)
                    num_set.add(repeat(i,n))
                i += 1
            # reset i for next n
            i = 1
            n += 1
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