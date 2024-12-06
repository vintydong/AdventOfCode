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

        # if "right" was seen, check if this was a path
        right_dir = dirs[(current_dir+1)%4]
        right_x = x + right_dir[0]
        right_y = y + right_dir[1]
        # if (right_x, right_y) in seen:
        #     print(f"{right_y}, {right_x} was seen!")
        seen_counts = 0
        while 0 < right_y < n and 0 < right_x < m and data[right_y][right_x] != '#':
            if (right_x, right_y) in seen:
                # print(f"Early stop at ({right_y}, {right_x})")
                seen_counts += 1
            right_x += right_dir[0]
            right_y += right_dir[1]
        else:
            # print(f"Stop at ({right_y}, {right_x})")
            # print(f"Adding {(x+dx,y+dy)}")
            if seen_counts > 1:
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