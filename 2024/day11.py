# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
from collections import Counter
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return list(map(int, puzzle_input.split(' ')))

def part1(data):
    """Solve part 1."""
    data = [x for x in data]
    for _ in range(25):
        # batch insert at the end
        inserts = []
        i = 0
        while i < len(data):
            stone = data[i]

            digits = 0
            while stone > 0:
                digits += 1
                stone = stone // 10

            if data[i] == 0:
                data[i] = 1
            elif digits & 1 == 0:
                h1 = str(data[i])[:digits//2]
                h2 = str(data[i])[digits//2:]
                data[i] = int(h1)
                inserts.append((i+1, int(h2)))
            else:
                data[i] *= 2024

            i += 1

        offset = 0
        for index, val in inserts:
            data.insert(index + offset, val)
            offset += 1
    return len(data)

def part2(data):
    """Solve part 2."""
    f = {0: 1} # store f(stone) = stone'
    stones = Counter(data)

    for iter in range(75):
        # print("Iter", iter)
        new_stones = Counter()
        for stone, count in stones.items():
            if stone in f:
                blinked = f[stone]
                if type(blinked) is tuple:
                    h1, h2 = blinked
                    new_stones[h1] += count
                    new_stones[h2] += count
                else:
                    new_stones[blinked] += count
            elif len(str(stone)) % 2 == 0:
                digits = len(str(stone))
                h1 = int(str(stone)[:digits//2])
                h2 = int(str(stone)[digits//2:])
                f[stone] = (h1, h2)
                new_stones[h1] += count
                new_stones[h2] += count
            else:
                product = stone * 2024
                f[stone] = product
                new_stones[product] += count 

        stones = new_stones
    return sum([stone for stone in stones.values()])

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