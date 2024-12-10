# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return list(map(lambda x: int(x), list(puzzle_input)))

def part1(data):
    """Solve part 1."""
    data = [x for x in data]
    left, right = 0, len(data) - 1
    if right & 1 == 1:
        right -= 1

    checksum = 0
    block_index = 0
    while left < right:
        while data[left] == 0 or left & 1 == 0:
            if left & 1 == 0:
                block_id = left // 2
                n = data[left]
                while n > 0:
                    checksum += (block_index * block_id)
                    n -= 1
                    block_index += 1
            left += 1
        
        if left >= right:
            break
        
        # left @ free block
        if data[left] >= data[right]:
            data[left] -= data[right]
            n = data[right]
            data[right] = 0
        else:
            data[right] -= data[left]
            n = data[left]
            data[left] = 0
        block_id = right // 2
        while n > 0:
            checksum += (block_index * block_id)
            n -= 1
            block_index += 1

        if data[right] == 0:
            right -= 2
    while data[left] != 0:
        if left & 1:
             left += 1
             continue
        n = data[left]
        block_id = left // 2
        while n > 0:
            checksum += (block_index * block_id)
            n -= 1
            block_index += 1
        left += 1
    return checksum

def part2(data):
    """Solve part 2."""
    # NOTE: i-th free space is at index (2*i + 1)
    # Index i (odd) is the ((i-1) // 2)-th free space
    right = len(data) - 1
    if right & 1 == 1:
        right -= 1

    checksum = 0
    free_spaces = [0] * (len(data) // 2)
    
    for i in range(len(free_spaces)):
        free_spaces[i] = {
            "block_ids": [],
            "length": data[2*i+1]
        }
    for right_block in range(right, -1, -2):
        # check if can move this file
        # check from left up to index of current block
        file_size = data[right_block]
        for j in range(len(free_spaces)):
            if 2 * j + 1 > right_block:
                break
            if free_spaces[j]["length"] >= file_size:
                block_id = right_block // 2
                free_spaces[j]["length"] -= file_size
                free_spaces[j]["block_ids"] += [block_id] * file_size
                data[right_block] = -file_size
                break

    # calculate checksum
    block_index = 0
    for i in range(0, len(data)):
        if i & 1:
            free_space_index = (i-1)//2
            for id in free_spaces[free_space_index]["block_ids"]:
                checksum += id * block_index
                block_index += 1
            block_index += free_spaces[free_space_index]["length"]
        else:
            # skip moved blocks
            if data[i] < 0:
                block_index += -data[i]
            # add blocks that weren't moved
            while data[i] > 0:
                checksum += (i // 2) * block_index
                block_index += 1
                data[i] -= 1
    return checksum

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