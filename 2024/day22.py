# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def next_secret_number(num):
    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num

def part1(data):
    """Solve part 1."""
    res = []
    for line in data: 
        num = int(line)
        for _ in range(2000):
            num = next_secret_number(num)
        res.append(num)
    return sum(res)

def part2(data):
    """Solve part 2."""
    # Brute force all possible 4-consecutive changes
    changes =  [-i for i in range(9, 0, -1)] + [i for i in range(10)]
    changes_prices = {}
    changes_bought = {}
    for w in changes:
        for x in changes:
            for y in changes:
                for z in changes:
                    changes_prices[(w, x, y, z)] = 0
                    changes_bought[(w, x, y, z)] = set()

    buyer_to_changes = {}
    buyer_to_number = {}

    for _ in range(2000):
        for i, line in enumerate(data):
            num = buyer_to_number.get(i, int(line))
            next_num = next_secret_number(num)

            curr_price = num % 10
            next_price = next_num % 10
            last_changes = buyer_to_changes.get(i, ())
            if len(last_changes) == 4:
                last_changes = (last_changes[1], last_changes[2], last_changes[3], next_price - curr_price)
            else:
                last_changes = last_changes + (next_price - curr_price,)

            buyer_to_changes[i] = last_changes
            if len(last_changes) == 4 and i not in changes_bought[last_changes]:
                changes_prices[last_changes] += next_price
                changes_bought[last_changes].add(i)

            buyer_to_number[i] = next_num
    return max(changes_prices.values())

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