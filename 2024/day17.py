# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse puzzle"""
    register_info, program = puzzle_input.split('\n\n')
    registers = map(int, re.findall(r'(\d+)', register_info))
    program = map(int, program.strip('Program: ').split(','))
    return list(registers), list(program)

def transform_operand(opcode, operand, registers):
    combos = {0, 2, 5, 6, 7}
    if opcode not in combos:
        return operand
    if operand == 7:
        raise ValueError("Invalid operand 7")
    elif operand > 3:
        operand = registers[operand - 4]
    return operand

def operation(opcode, operand, registers):
    A, B, C = 0, 1, 2
    
    operand = transform_operand(opcode, operand, registers)

    if opcode == 0:
        registers[A] = registers[A] >> operand
    elif opcode == 1:
        registers[B] = registers[B] ^ operand
    elif opcode == 2: 
        registers[B] = operand & 7
    elif opcode == 3:
        if registers[A] != 0:
            return ("JUMP", operand)
    elif opcode == 4:
        registers[B] = registers[B] ^ registers[C]
    elif opcode == 5:
        return ("PRINT", operand & 7)
    elif opcode == 6:
        registers[B] = registers[A] >> operand
    elif opcode == 7:
        registers[C] = registers[A] >> operand
    return ("NOOP", 0)

def part1(data):
    """Solve part 1."""
    registers, program = data
    outputs = []
    ip = 0
    while ip < len(program):
        opcode, operand = program[ip], program[ip+1]
        op, res = operation(opcode, operand, registers)
        if op == "JUMP":
            ip = res
            continue
        elif op == "PRINT":
            outputs.append(res)
        ip += 2
    return ','.join(map(str, outputs))

'''
Register A: 17323786
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0

2,4 - B = A & 7
1,1 - B = B ^ 1
7,5 - C = A >> B
1,5 - B = B ^ 5
4,1 - B = B ^ C
5,5 - PRINT(B & 7)
0,3 - A = A >> 3
3,0 - JUMP 0
'''
def run_vm(A, B, C):
    B = A & 7
    B = B ^ 1
    C = A >> B
    B = B ^ 5
    B = B ^ C
    return (B & 7)

# for smaller example
def run_vm_small(A, B, C):
    A = A >> 3
    return A & 7

def part2(data):
    """Solve part 2."""
    # Backtrack from back of output since last number depends on final 3 bits of A
    registers, program = data
    stack = [(1, i) for i in range(7,-1,-1)]
    while stack: 
        depth, val = stack.pop()
        target = program[-depth]
        vm_res = run_vm(val, 0, 0)
        if vm_res == target:
            if depth == len(program):
                return val
            stack.extend([(depth+1, (val << 3) + i) for i in range(7,-1,-1)])

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