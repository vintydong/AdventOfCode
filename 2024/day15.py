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
    grid = [[c for c in row] for row in grid]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
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

    seen = set()

    # Check a single part of box movable
    def check_movable(box):
        if box in seen:
            return True
        seen.add(box)
        x, y = box

        match grid[y+dy][x+dx]:
            case '#':
                return False
            case '[':
                return check_movable((x+dx, y+dy)) and check_movable((x+dx+1, y+dy))
            case ']':
                return check_movable((x+dx, y+dy)) and check_movable((x+dx-1, y+dy))
            case '.': 
                return True
        return True
    
    if not check_movable((bx-dx, by-dy)):
        return False
    
    while len(seen) > 0:
        print(seen)
        for x, y in seen.copy():
            nx, ny = x + dx, y + dy
            if (nx, ny) not in seen:
                if grid[ny][nx] != '@' and grid[y][x] != '@':
                    grid[ny][nx] = grid[y][x]
                    grid[y][x] = '.'
                seen.remove((x,y))
    
    return True

i = 0
def run_part2(grid, start, moves):
    move_dict = {
        '^': (0,-1),
        'v': (0,1),
        '<': (-1,0),
        '>': (1,0)
    }

    x, y = start
    STARTING_MOVE = 12435123
    global i

    for move in moves:
        dx, dy = move_dict[move]
        if i > STARTING_MOVE:
            print(f"Current Pos {(y,x)}. Move: {move}")
            print(f"Checking future {(y+dy,x+dx)}: {grid[y+dy][x+dx]}")
        noop = False

        if grid[y+dy][x+dx] == '#':
            noop = True
        elif grid[y+dy][x+dx] in '[]':
            if move_boxes_part2(grid, (dx,dy), (x+dx,y+dy)):
                if grid[y+dy][x+dx] in '[]':
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
        if i > STARTING_MOVE:
            print(f"Move {i}: {move}")
            print_grid(grid)
        i += 1

def part2(data):
    """Solve part 2."""
    grid, moves = data
    grid = [[c for c in row] for row in grid]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
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
    # solution1 = part1(data)
    solution2 = part2(data)

    return 0, solution2

if __name__ == "__main__":
    path = 'input.txt'
    if len(sys.argv) > 1 and sys.argv[1]:
        path = 'input2.txt'

    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))