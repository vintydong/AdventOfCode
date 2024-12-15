# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse puzzle"""
    def line_to_vecs(line):
        return list(map(int, re.findall(r'(-?\d+)', line)))
    return list(map(line_to_vecs, puzzle_input.split('\n')))

def part1(data):
    """Solve part 1."""
    m, n = 103, 101
    positions = [list(m) for m in data]
    for bot in positions:
        x, y, vx, vy = bot
        bot[0] = (x + 100*vx) % n
        bot[1] = (y + 100*vy) % m

    yaxis = m // 2
    xaxis = n // 2
    quadrants = [0, 0, 0, 0]

    for bot in positions:
        x, y, vx, vy = bot
        if x < xaxis and y < yaxis:
            quadrants[0] += 1
        elif x < xaxis and y > yaxis:
            quadrants[1] += 1
        elif x > xaxis and y < yaxis:
            quadrants[2] += 1
        elif x > xaxis and y > yaxis:
            quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

'''
--- Part Two ---

During the bathroom break, someone notices that these robots seem awfully similar to ones built and used at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to display the Easter egg?

???????????
'''

def print_grid(grid):
    m, n = len(grid), len(grid[0])
    for row in grid:
        print(''.join(['|'] + ['.' if c > 0 else ' ' for c in row] + ['|']))

def part2(data):
    """Solve part 2."""
    from scipy.signal import convolve2d
    import numpy as np

    window = np.ones((3,3))
    m, n = 103, 101
    positions = [list(m) for m in data]

    N = 10000
    iterations = np.zeros(N)
    for i in range(N):
        grid = np.zeros((m,n))
        for bot in positions:
            x, y, vx, vy = bot
            bot[0] = (x + vx) % n
            bot[1] = (y + vy) % m
            grid[bot[1]][bot[0]] = 1
        convolution = convolve2d(grid, window)
        iterations[i] = np.sum(convolution)

        if i == 7571: # checking printed out argmax
            print_grid(grid)
    print(iterations)
    print(np.max(iterations), np.argmax(iterations))

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