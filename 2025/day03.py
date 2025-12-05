import pathlib
import sys

'''
Part 1: Greedy solution for 2 digits
Part 2: Greedy solution for n = 12 digits

Select the largest digit that isn't too far to the right
- allows at least n-1 digits left
'''

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def part1(data):
    """Solve part 1."""
    total = 0
    for bank in data:
        # Look for largest number from 0 to n-1
        first = max(bank[:-1])
        first_index = bank.index(first)
        second = max(bank[first_index+1:])
        total += int(first + second)
    return total

def part2(data):
    """Solve part 2."""
    total = 0
    for bank in data:
        n = 12
        substr = bank
        curr = ""
        while n > 1:
            curr_max = max(substr[:-(n-1)])
            curr_max_index = substr.index(curr_max)
            n -= 1
            curr += curr_max
            substr = substr[curr_max_index+1:]
        curr += max(substr)
        total += int(curr)
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