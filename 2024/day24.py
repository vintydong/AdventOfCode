# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys
import graphviz

def parse(puzzle_input):
    """Parse puzzle"""
    variable_lines, gates_lines = puzzle_input.split('\n\n')
    variable_lines = [line.split(':') for line in variable_lines.split('\n')]
    variables = {line[0]: int(line[1].strip()) for line in variable_lines}

    gates = set()
    for line in gates_lines.split('\n'):
        inputs, output = line.split(' -> ')
        a, op, b = inputs.split(' ')
        gates.add((a, op, b, output))
    
    return variables, gates

def part1(data):
    """Solve part 1."""
    variables, gates = data
    gates = gates.copy()
    z_vars = set()
    while len(gates) > 0:
        a, op, b, output = gates.pop()
        if a in variables and b in variables:
            if op == 'AND':
                variables[output] = variables[a] & variables[b]
            elif op == 'OR':
                variables[output] = variables[a] | variables[b]
            elif op == 'XOR':
                variables[output] = variables[a] ^ variables[b]

            if output.startswith('z'):
                z_vars.add(output)
        else:
            gates.add((a, op, b, output))
    res = ''.join([str(variables[z]) for z in sorted(z_vars, reverse=True)])
    return int(res, 2)

"""
x 0100000010100011101110001001000100010110100011
y 0100010110001100010000100010101101111011001101
part 1 z
z 1000011001000000000000101011101110000001110000
correct z
z 1000011000101111111110101011110010010001110000
"""
def part2(data):
    """Solve part 2."""
    variables, gates = data
    wrong = set()
    highest_z = "z45"
    for op1, op, op2, res in gates:
        if res[0] == "z" and op != "XOR" and res != highest_z:
            wrong.add(res)
        if (
            op == "XOR"
            and res[0] not in ["x", "y", "z"]
            and op1[0] not in ["x", "y", "z"]
            and op2[0] not in ["x", "y", "z"]
        ):
            wrong.add(res)
        if op == "AND" and "x00" not in [op1, op2]:
            for subop1, subop, subop2, subres in gates:
                if (res == subop1 or res == subop2) and subop != "OR":
                    wrong.add(res)
        if op == "XOR":
            for subop1, subop, subop2, subres in gates:
                if (res == subop1 or res == subop2) and subop == "OR":
                    wrong.add(res)
    return ','.join(sorted(wrong))

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