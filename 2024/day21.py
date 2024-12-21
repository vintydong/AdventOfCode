# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
from collections import deque
from functools import lru_cache
import pathlib
import sys
import math

numpad = [[7,8,9],[4,5,6],[1,2,3],[-1,0,'A']]
dirpad = [[-1,'^', 'A'],['<', 'v', '>']]
numpad_to_positions = {}
dirpad_to_positions = {}
for y, row in enumerate(numpad):
    for x, char in enumerate(row):
        numpad_to_positions[str(char)] = (x,y)

for y, row in enumerate(dirpad):
    for x, char in enumerate(row):
        if char != '-1':
            dirpad_to_positions[char] = (x,y)

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

@lru_cache(maxsize=None)
def get_cheapest_dirpad_path(start, end, robots):
    # Explore all possible paths to get to the dir at end and find shortest
    res = math.inf
    queue = deque([(start[0], start[1], "")])
    endx, endy = end
    while len(queue) > 0:
        x, y, path = queue.popleft()
        if (x,y) == end:
            # this path needs to be reached by a robot so recurse one down
            res = min(res, get_cheapest_dirpad(path + "A", robots-1)) 
        elif dirpad[y][x] != -1:
            if x > endx:
                queue.append((x-1, y, path + "<"))
            elif x < endx:
                queue.append((x+1, y, path + ">"))
            if y > endy:
                queue.append((x, y-1, path + "^"))
            elif y < endy:
                queue.append((x, y+1, path + "v"))
    return res

def get_cheapest_dirpad(path, robots):
    if robots <= 1:
        return len(path)
    res = 0
    current_pos = (2,0)
    for node in path:
        xx, yy = dirpad_to_positions[node]
        res += get_cheapest_dirpad_path(current_pos, (xx,yy), robots)
        current_pos = (xx,yy)
    return res

def get_cheapest_path(start, end, robots):
    # Explore all possible paths to get to the num at end and find shortest
    res = math.inf
    queue = deque([(start, "")])
    endx, endy = end
    while len(queue) > 0:
        node, path = queue.popleft()
        x, y = node
        if (x,y) == end:
            res = min(res, get_cheapest_dirpad(path + "A", robots))
        elif numpad[y][x] != -1:
            if x > endx:
                queue.append(((x-1, y), path + "<"))
            elif x < endx:
                queue.append(((x+1, y), path + ">"))
            if y > endy:
                queue.append(((x, y-1), path + "^"))
            elif y < endy:
                queue.append(((x, y+1), path + "v"))
    return res

def get_complexity(codes, robots):
    complexity = 0
    for code in codes:
        res = 0
        current_pos = (2,3)
        for char in code:
            xx, yy = numpad_to_positions[char]
            res += get_cheapest_path(current_pos, (xx,yy), robots)
            current_pos = (xx,yy)
        complexity += res * int(code[:-1])
    return complexity

def part1(data):
    """Solve part 1."""
    return get_complexity(data, robots=3)

def part2(data):
    """Solve part 2."""
    return get_complexity(data, robots=26)

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