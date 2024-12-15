# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def get_adjacent(data, x, y):
    m, n = len(data), len(data[0])
    diffs = [(-1,0),(1,0),(0,1),(0,-1)]
    adjacent = []
    for dx, dy in diffs:
        if -1 < x + dx < n and -1 < y + dy < m:
            adjacent.append((x+dx, y+dy))
    return adjacent

def get_region_set(data, x, y):
    visited = set()
    stack = [(x,y)]
    region_char = data[y][x]
    visited.add((x,y))
    while stack:
        i,j = stack.pop()
        visited.add((i,j))
        adjacent = get_adjacent(data, i, j)

        for x,y in adjacent:
            if (x,y) not in visited and data[y][x] == region_char:
                stack.append((x,y))

    return visited

def part1(data):
    """Solve part 1."""
    global_visited = set()
    total_price = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x,y) in global_visited:
                continue

            current_region = get_region_set(data, x, y)
            area = len(current_region)
            perim = 0
            for node in current_region:
                if node in global_visited:
                    break
                adjacents = get_adjacent(data, node[0], node[1])
                for xx, yy in adjacents:
                    if data[yy][xx] == char:
                        continue
                    perim += 1
                perim += 4 - len(adjacents)
            total_price += area * perim
            global_visited.update(current_region)
    return total_price


def part2(data):
    """Solve part 2."""
    global_visited = set()
    total_price = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x,y) in global_visited:
                continue

            current_region = get_region_set(data, x, y)
            area = len(current_region)
            perim = 0

            if area == 1 or area == 2:
                perim = 4
            else:
                for node in current_region:
                    xx, yy = node
                    # Convex corners
                    perim += (xx+1, yy) not in current_region and (xx, yy-1) not in current_region
                    perim += (xx-1, yy) not in current_region and (xx, yy+1) not in current_region
                    perim += (xx+1, yy) not in current_region and (xx, yy+1) not in current_region
                    perim += (xx-1, yy) not in current_region and (xx, yy-1) not in current_region
                    # Concave corners
                    perim += (xx-1, yy) in current_region and (xx, yy-1) in current_region and (xx-1, yy-1) not in current_region
                    perim += (xx+1, yy) in current_region and (xx, yy-1) in current_region and (xx+1, yy-1) not in current_region
                    perim += (xx-1, yy) in current_region and (xx, yy+1) in current_region and (xx-1, yy+1) not in current_region
                    perim += (xx+1, yy) in current_region and (xx, yy+1) in current_region and (xx+1, yy+1) not in current_region
            total_price += area * perim
            global_visited.update(current_region)
    return total_price

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