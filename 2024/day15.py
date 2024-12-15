# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    grid, moves = puzzle_input.split('\n\n')
    return [list(line) for line in grid.split('\n')], ''.join(moves.split('\n'))

def print_grid(grid):
    for row in grid:
        print(''.join(['|'] + row + ['|']))
    print('\n')

def move_boxes(grid, dir, box) -> bool:
    dx, dy = dir
    bx, by = box

    if grid[by][bx] != 'O':
        raise RuntimeError(f"No box at {(by, bx)}; it is {grid[by][bx]}")

    tempx, tempy = bx, by
    while grid[tempy][tempx] != '.':
        if grid[tempy][tempx] == '#':
            return False

        tempx += dx
        tempy += dy
    
    # Go backwards, moving boxes forwards
    tempx, tempy = tempx - dx, tempy - dy
    while grid[tempy][tempx] == 'O':
        grid[tempy+dy][tempx+dx] = 'O'
        grid[tempy][tempx] = '.'
        tempx -= dx
        tempy -= dy
    return True


def run(grid, start, moves):
    move_dict = {
        '^': (0,-1),
        'v': (0,1),
        '<': (-1,0),
        '>': (1,0)
    }
    
    i = 0
    x, y = start
    for move in moves:
        dx, dy = move_dict[move]
        # print(f"Checking future {(y+dy,x+dx)}: {grid[y+dy][x+dx]}")
        noop = False

        if grid[y+dy][x+dx] == '#':
            noop = True
        elif grid[y+dy][x+dx] == 'O':
            if move_boxes(grid, (dx,dy), (x+dx,y+dy)):
                if grid[y+dy][x+dx] == 'O':
                    raise RuntimeError("Did not move box")
                grid[y][x] = '.'
                grid[y+dy][x+dx] = '@'
                noop = False
            else:
                noop = True
        elif grid[y+dy][x+dx] == '.':
            grid[y+dy][x+dx] = '@'
            grid[y][x] = '.'
            noop = False

        if not noop:
            x, y = x+dx, y+dy

        # print(f"Move {i}: {move}")
        # print_grid(grid)
        i += 1

def part1(data):
    """Solve part 1."""
    grid, moves = data
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "@":
                start = (x,y)
                
    run(grid, start, moves)

    total = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                total += 100 * y + x
    return total

def move_boxes_part2(grid, dir, box) -> bool:
    dx, dy = dir
    bx, by = box

    if grid[by][bx] != '[' and grid[by][bx] != ']':
        raise RuntimeError(f"No box at {(by, bx)}; it is {grid[by][bx]}")

    # symbolic left, right representing the ends of the span of boxes when up/down
    vertical_move = False
    if dir == (0, 1) or dir == (0, -1):
        vertical_move = True
        if grid[by][bx] == '[':
            left, right = by, by+1
        elif grid[by][bx] == ']':
            left, right = by-1, by

    tempx, tempy = bx, by
    while grid[tempy][tempx] != '.':
        if grid[tempy][tempx] == '#':
            return False
        

        tempx += dx
        tempy += dy
    
    # Go backwards, moving boxes forwards
    tempx, tempy = tempx - dx, tempy - dy
    while grid[tempy][tempx] == '[' or grid[tempy][tempx] == ']':
        grid[tempy+dy][tempx+dx] = 'O'
        grid[tempy][tempx] = '.'
        tempx -= dx
        tempy -= dy
    return True

def run_part2(grid, start, moves):
    move_dict = {
        '^': (0,-1),
        'v': (0,1),
        '<': (-1,0),
        '>': (1,0)
    }
    
    i = 0
    x, y = start
    for move in moves:
        dx, dy = move_dict[move]
        # print(f"Checking future {(y+dy,x+dx)}: {grid[y+dy][x+dx]}")
        noop = False

        if grid[y+dy][x+dx] == '#':
            noop = True
        elif grid[y+dy][x+dx] == '[' or grid[y+dy][x+dx] == ']':
            if move_boxes(grid, (dx,dy), (x+dx,y+dy)):
                if grid[y+dy][x+dx] == '[' or grid[y+dy][x+dx] == ']':
                    raise RuntimeError("Did not move box")
                grid[y][x] = '.'
                grid[y+dy][x+dx] = '@'
                noop = False
            else:
                noop = True
        elif grid[y+dy][x+dx] == '.':
            grid[y+dy][x+dx] = '@'
            grid[y][x] = '.'
            noop = False

        if not noop:
            x, y = x+dx, y+dy

        # print(f"Move {i}: {move}")
        # print_grid(grid)
        i += 1

def part2(data):
    """Solve part 2."""
    grid, moves = data
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "@":
                start = (x,y)
                
    run_part2(grid, start, moves)

    total = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "[":
                total += 100 * y + x
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