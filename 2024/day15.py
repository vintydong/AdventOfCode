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

    is_up = by + dy > by

    if grid[by][bx] != '[' and grid[by][bx] != ']':
        raise RuntimeError(f"No box at {(by, bx)}; it is {grid[by][bx]}")

    # symbolic left, right representing the ends of the span of boxes when up/down
    vertical_move = False
    if dir == (0, 1) or dir == (0, -1):
        vertical_move = True
        if grid[by][bx] == '[':
            left, right = bx, bx+1
        elif grid[by][bx] == ']':
            left, right = bx-1, bx
    else:
        left, right = bx, bx

    tempx, tempy = bx, by

    while True:
        if vertical_move:
            tl = left
            tr = right
            all_empty = True
            while tl < tr + 1:
                if grid[tempy][tl] == '#':
                    return False
                if grid[tempy][tl] != '.':
                    all_empty = False
                tl += 1

            if all_empty:
                break
            
            # handle disconnected cases; no need to expand window
            if grid[tempy][left] == ']' and grid[tempy-dy][left] in '[]':
                left = left - 1
            if grid[tempy][right] == '[' and grid[tempy-dy][right] in '[]':
                right = right + 1
        else:
            if grid[tempy][tempx] == '#':
                return False
            elif grid[tempy][tempx] == '.':
                break
        tempx += dx
        tempy += dy
    
    # Go backwards, moving boxes forwards
    tempx, tempy = tempx - dx, tempy - dy
    while grid[tempy][tempx] == '[' or grid[tempy][tempx] == ']' or (vertical_move and (is_up and tempy > by or not is_up and tempy < by)):
        if vertical_move:
            tx = left
            while tx < right + 1:
                if grid[tempy][tx] == ']' and tx == left:
                    tx += 1 
                    continue
                if grid[tempy][tx] == '[' and tx == right:
                    tx += 1
                    continue
                if grid[tempy][tx] in '[]':
                    grid[tempy+dy][tx+dx] = grid[tempy][tx]
                    grid[tempy][tx] = '.'
                tx += 1
        elif grid[tempy][tempx] == '[' or grid[tempy][tempx] == ']':
            grid[tempy+dy][tempx+dx] = grid[tempy][tempx]
            grid[tempy][tempx] = '.'

        tempx -= dx
        tempy -= dy
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
    STARTING_MOVE = 111111
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