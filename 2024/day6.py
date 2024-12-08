import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def part1(data):
    """Solve part 1."""
    seen = set()
    m, n = len(data), len(data[0])
    for row in range(m): 
        for col in range(n):
            if data[row][col] == '^':
                y, x = row, col
                break
            # grid[row][col] = data[row][col]
    
    seen.add((x,y))
    dirs = [(0,-1),(1,0),(0,1),(-1,0)]
    current_dir = 0
    while -1 < x < n and -1 < y < m:
        if data[y][x] == '#':
            x, y = x - dx, y - dy
            current_dir = (current_dir + 1) % 4
        else:
            seen.add((x,y))
        
        dx, dy = dirs[current_dir]
        x, y = x + dx, y + dy
    return len(seen)

def check_loop(start, data, obstacle, current_dir):
    seen = {}
    m, n = len(data), len(data[0])
    y, x = start
    dirs = [(0,-1),(1,0),(0,1),(-1,0)]
    dx, dy = dirs[current_dir]
    while -1 < x < n and -1 < y < m:
        if data[y][x] == '#' or (y,x) == obstacle:
            # keep track of which dir this square was visited
            x, y = x - dx, y - dy
            current_dir = (current_dir + 1) % 4
            continue
        if (x,y) in seen:
            # if same dir, then we've taken this path before => loop
            if current_dir in seen[(x,y)]:
                return True
            seen[(x,y)].add(current_dir)
        else:
            seen[(x,y)] = set([current_dir])
        dx, dy = dirs[current_dir]

        x, y = x + dx, y + dy
    return False

def part2(data):
    """Solve part 2."""
    seen = set()
    m, n = len(data), len(data[0])
    for row in range(m): 
        for col in range(n):
            if data[row][col] == '^':
                y, x = row, col
                break
            # grid[row][col] = data[row][col]
    
    seen.add((x,y))
    dirs = [(0,-1),(1,0),(0,1),(-1,0)]
    current_dir = 0
    obstacles = set()
    while -1 < x < n and -1 < y < m:
        if data[y][x] == '#':
            x, y = x - dx, y - dy
            current_dir = (current_dir + 1) % 4
            continue

        seen.add((x,y))
        dx, dy = dirs[current_dir]

        # at every step, simulate going right
        # except if it blocks the path already taken
        if (x+dx, y+dy) not in seen and (x+dx, y+dy) not in obstacles:
            right_dir = (current_dir+1) % 4
            # print("Checking obstacle at", (y+dy, x+dx))
            if check_loop((y, x), data, (y+dy, x+dx), right_dir):
                obstacles.add((x+dx,y+dy))

        x, y = x + dx, y + dy
    return len(obstacles)


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