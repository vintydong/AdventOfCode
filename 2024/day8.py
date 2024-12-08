# Template: https://realpython.com/python-advent-of-code/#a-starting-template
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    return puzzle_input.split('\n')

def get_freq_to_pos(data):
    freq_to_pos = {}
    for i, line in enumerate(data): 
        for j, char in enumerate(line):
            if char == '.':
                continue

            if char in freq_to_pos:
                freq_to_pos[char].add((i,j))
            else:
                freq_to_pos[char] = set([(i,j)])
    return freq_to_pos

def in_bounds(m, n, y, x):
    return -1 < y < m and -1 < x < n

def part1(data):
    """Solve part 1."""
    freq_to_pos = get_freq_to_pos(data)
    antinodes = set()
    m, n = len(data), len(data[0])
    for freq in freq_to_pos.keys():
        # generate nodes for all n choose 2 for particular freq
        antennas = list(freq_to_pos[freq])
        for i, i_pos in enumerate(antennas):
            for j, j_pos in enumerate(antennas[i+1:]):
                dy, dx = (i_pos[a] - j_pos[a] for a in range(2))
                
                a1y, a1x = i_pos[0] + dy, i_pos[1] + dx
                a2y, a2x = j_pos[0] - dy, j_pos[1] - dx

                if in_bounds(m, n, a1y, a1x):
                    antinodes.add((a1y, a1x))
                if in_bounds(m, n, a2y, a2x):
                    antinodes.add((a2y, a2x))
    return len(antinodes)

def part2(data):
    """Solve part 2."""
    freq_to_pos = get_freq_to_pos(data)
    antinodes = set()
    m, n = len(data), len(data[0])
    for freq in freq_to_pos.keys():
        # generate nodes for all n choose 2 for particular freq
        antennas = list(freq_to_pos[freq])
        for i, i_pos in enumerate(antennas):
            for j, j_pos in enumerate(antennas[i+1:]):
                dy, dx = (i_pos[a] - j_pos[a] for a in range(2))
                
                a1y, a1x = i_pos[0] + dy, i_pos[1] + dx
                while in_bounds(m, n, a1y, a1x):
                    antinodes.add((a1y, a1x))
                    a1y, a1x = a1y + dy, a1x + dx
                a2y, a2x = j_pos[0] - dy, j_pos[1] - dx
                while in_bounds(m, n, a2y, a2x):
                    antinodes.add((a2y, a2x))
                    a2y, a2x = a2y - dy, a2x - dx

        for a in antennas:
            antinodes.add(a)
    return len(antinodes)

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