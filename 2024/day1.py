import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    lines = puzzle_input.split('\n')
    length = len(lines)
    list1, list2 = [0] * length, [0] * length
    for i, line in enumerate(lines):
        j, k = line.split()
        list1[i], list2[i] = int(j), int(k)
    return list1, list2

def part1(data):
    """Solve part 1."""
    list1, list2 = data
    list1.sort()
    list2.sort()

    s = 0
    for i in range(len(list1)):
        s = s + abs(list1[i] - list2[i])
    return s

def part2(data):
    """Solve part 2."""
    list1, list2 = data
    right_counts = {}
    for i in list2:
        right_counts[i] = right_counts.get(i, 0) + 1
    
    s = 0
    for i in list1:
        s = s + right_counts.get(i, 0) * i
    return s

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    print(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))