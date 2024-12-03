import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input

def part1(data):
    """Solve part 1."""
    import re
    matches = re.findall(r'mul\((\d+),(\d)+\)', data)
    s = 0
    for x,y in matches:
        s += int(x) * int(y)
    return s

def part2(data):
    """Solve part 2."""
    import re
    matches = re.findall(r"(mul\((\d+)\,(\d+)\)|do\(\)|don't\(\))", data)
    s = 0
    doing = True
    for string,x,y in matches:
        if string == "don't()":
            doing = False
        elif string == "do()":
            doing = True
        elif doing:
            s += int(x) * int(y)
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