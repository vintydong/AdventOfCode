import pathlib

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def part1(data):
    """Solve part 1."""
    s = 0
    uncalibrated = []
    for line in data:
        if line.strip() != '':
            test_val, nums = line.split(':')
        else:
            continue
        nums = nums.strip().split(' ')
        nums = [int(x) for x in nums]
        max_operator = 1 << len(nums) - 1
        n = 0
        while n < max_operator:
            curr_sum = nums[0]
            index = 1
            while index < len(nums):
                bit = n & (1 << (index - 1))
                if bit != 0:
                    curr_sum = curr_sum + nums[index]
                else:
                    curr_sum = curr_sum * nums[index]
                index += 1
            if curr_sum == int(test_val):
                s += int(test_val)
                break
            n += 1
        else:
            uncalibrated.append(line)
    return s, uncalibrated


def part2(data):
    """Solve part 2."""
    s = 0
    def _add(a, b):
        return a + b
    def _mul(a, b):
        return a * b
    def _cat(a, b):
        return int(str(a) + str(b))
    def test(res, x, nums):
        ops = [_add, _mul, _cat]
        def _test(x, nums):
            if len(nums) < 1:
                return x == res
            boo = any([_test(op(x, nums[0]), nums[1:]) for op in ops])
            return boo
        return _test(x, nums)
    
    for line in data:
        if line.strip() != '':
            test_val, nums = line.split(':')
        else:
            continue
        nums = [int(x) for x in nums.strip().split(' ')]

        check = test(int(test_val), nums[0], nums[1:])
        if check:
            s += int(test_val)
    return s

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1, uncalibrated = part1(data)
    solution2 = part2(uncalibrated)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = pathlib.Path('input.txt').read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))