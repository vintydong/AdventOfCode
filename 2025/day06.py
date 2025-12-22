import pathlib
import sys

'''
Part 1: Simple parsing the rows
Part 2: Split on the symbols and parse the columns up to next symbol
'''


def parse(puzzle_input):
    """Parse puzzle"""
    print(len(puzzle_input[-1]))
    return puzzle_input.split('\n')

def mult(arr):
    total = 1
    for n in arr:
        total *= n
    return total

def part1(data):
    """Solve part 1."""
    data = [row.split() for row in data]
    rows = len(data)
    cols = len(data[0])
    total = 0
    for i in range(cols):
        op = data[rows-1][i]
        if op == '+':
            answer = 0
            for j in range(rows-1):
                answer += int(data[j][i])
        elif op == '*':
            answer = 1
            for j in range(rows-1):
                answer *= int(data[j][i])
        total += answer
    return total


def part2(data):
    """Solve part 2."""
    rows = len(data)
    cols = len(data[-1])
    problems = [row.split() for row in data]

    last_op_index = cols;
    total = 0;
    i = cols-1;

    while i >= 0:
        while i >= 0 and data[-1][i] != '+' and data[-1][i] != '*':
            i -= 1

        if i < 0:
            break
        
        # Add up the numbers before the last operator
        nums = []
        j = i
        while j <= last_op_index-1:
            s = ""
            for r in range(rows-1):
                s += data[r][j]
            if not s.strip():
                break
            s = int(s)
            nums.append(s)
            j += 1
        answer = 0
        if data[rows-1][i] == '+':
            answer = sum(nums)
        elif data[rows-1][i] == '*':
            answer = mult(nums)

        total += answer 
        last_op_index = i
        i = i - 1

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

    puzzle_input = pathlib.Path(path).read_text()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))