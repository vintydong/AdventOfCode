import pathlib
import sys

'''
Part 1: Precompute all distances between points, merge circuits each connection
Part 2: Connect until all points are connected
'''

def parse(puzzle_input):
    """Parse puzzle"""
    return sorted([tuple(map(int, line.split(','))) for line in puzzle_input.split('\n')])

def shortest_pair(points, connected):
    '''
    Shortest pair of points not in connected
    Used for part 1 example
    Replaced by pre-computing all distances
    '''
    min_pair = ((0,0,0),(0,0,0))
    min_d = float('inf')

    for x,y,z in points:
        for x2,y2,z2 in points:
            if (x,y,z) == (x2,y2,z2) or ((x,y,z), (x2,y2,z2)) in connected:
                continue
            d = (x-x2) ** 2 + (y-y2) ** 2 + (z-z2) ** 2
            if d < min_d:
                min_d = d
                min_pair = ((x,y,z),(x2,y2,z2))
    return min_pair

def all_distances(points):
    '''
    Precompute distance between all pair of points sorted by distance
    '''
    distances = []
    for x,y,z in points:
        for x2,y2,z2 in points:
            if (x,y,z) == (x2,y2,z2):
                continue
            d = (x-x2) ** 2 + (y-y2) ** 2 + (z-z2) ** 2
            point_pair = ((x,y,z), (x2,y2,z2))
            distances.append((d, point_pair))
    distances.sort()
    return distances

def connect_points(data, n):
    connected = set()
    circuits = {}
    data = sorted(data)

    distances = all_distances(data)
    distance_index = 0

    for _ in range(n):
        while distances[distance_index][1] in connected:
            distance_index += 1
        _d, pair = distances[distance_index]

        connected.add(pair)
        connected.add(pair[::-1])

        partial_circuit = set([pair[0], pair[1]])
        merged_circuit = circuits.get(pair[0], set()) | circuits.get(pair[1], set()) | partial_circuit

        for circuit in merged_circuit:
            circuits[circuit] = merged_circuit
    return circuits

def part1(data):
    """Solve part 1."""
    circuits = connect_points(data, 1000)

    sorted_circuits = dict(sorted(circuits.items(), key=lambda x: -len(x[1])))

    processed = set()
    total = 1
    count = 0
    for circuit in sorted_circuits:
        if count == 3:
            return total
        
        if circuit in processed:
            continue

        total *= len(sorted_circuits[circuit])
        count += 1
        for point in sorted_circuits[circuit]:
            processed.add(point)
    return total

def part2(data):
    """Solve part 2."""
    connected = set()
    circuits = {}
    data = sorted(data)

    distances = all_distances(data)
    distance_index = 0

    while True:
        while distances[distance_index][1] in connected:
            distance_index += 1
        _d, pair = distances[distance_index]

        connected.add(pair)
        connected.add(pair[::-1])

        partial_circuit = set([pair[0], pair[1]])
        merged_circuit = circuits.get(pair[0], set()) | circuits.get(pair[1], set()) | partial_circuit

        if len(merged_circuit) == len(data):
            return pair[0][0] * pair[1][0]

        for circuit in merged_circuit:
            circuits[circuit] = merged_circuit

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