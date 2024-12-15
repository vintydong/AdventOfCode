# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys
import numpy as np
import re

def parse(puzzle_input):
    """Parse puzzle"""
    lines = puzzle_input.split('\n')
    problems = []
    for i in range(0, len(lines), 4):
        a_button = re.match(r'X\+(\d+), Y\+(\d+)', lines[i].split(':')[1].strip())
        b_button = re.match(r'X\+(\d+), Y\+(\d+)', lines[i+1].split(':')[1].strip())
        prize = re.match(r'X=(\d+), Y=(\d+)', lines[i+2].split(':')[1].strip())

        problems.append(list(map(int, [
            a_button[1],
            a_button[2],
            b_button[1],
            b_button[2],
            prize[1],
            prize[2]
        ])))
    return problems

def part1(data):
    """Solve part 1."""
    cost = 0
    for problem in data:
        ax, ay, bx, by, px, py = problem
        matrix = np.array([
            [ax, bx],
            [ay, by]
        ])
        rhs = np.array([[px], [py]])
        sol = np.linalg.solve(matrix, rhs)
        a,b = sol.reshape(2)

        # Check if integer solution
        if abs(a - round(a)) < 1e-4 and abs(b - round(b)) < 1e-4:
            cost += 3*a + b
    return int(cost)

def part2(data):
    """Solve part 2."""
    cost = 0
    for problem in data:
        ax, ay, bx, by, px, py = problem
        matrix = np.array([
            [ax, bx],
            [ay, by]
        ])
        rhs = np.array([[px+10000000000000], [py+10000000000000]])
        sol = np.linalg.solve(matrix, rhs)
        a,b = sol.reshape(2)

        # Check if integer solution
        if abs(a - round(a)) < 1e-4 and abs(b - round(b)) < 1e-4:
            cost += 3*a + b
    return int(cost)

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