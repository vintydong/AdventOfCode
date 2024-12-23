# Original template: https://realpython.com/python-advent-of-code/#a-starting-template
# Modified by @vintydong
import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    lines = puzzle_input.split('\n')
    data = [line.split('-') for line in lines]
    return data

def part1(data):
    """Solve part 1."""
    nodes = set()
    graph = {}
    for edge in data:
        a, b = edge
        nodes.add(a)
        nodes.add(b)
        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = set([b])
        
        if b in graph:
            graph[b].add(a)
        else:
            graph[b] = set([a])
    
    # Look for sets of 3
    interconnected = set()
    for node in nodes:
        for n1 in graph[node]:
            for n2 in graph[n1]:
                if n2 != node and n2 in graph[node]:
                    interconnected.add(tuple(sorted([node, n1, n2])))
    count = 0
    for k in interconnected:
        n1, n2, n3 = k
        if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
            count += 1
    return count  

def part2(data):
    """Solve part 2."""
    nodes = set()
    graph = {}
    for edge in data:
        a, b = edge
        nodes.add(a)
        nodes.add(b)
        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = set([b])
        
        if b in graph:
            graph[b].add(a)
        else:
            graph[b] = set([a])
    
    # Look for sets of 3
    interconnected = set()
    for node in nodes:
        for n1 in graph[node]:
            for n2 in graph[n1]:
                if n2 != node and n2 in graph[node]:
                    interconnected.add(tuple(sorted([node, n1, n2])))
    
    # Try expanding size of cliques
    max_clique_size = 3
    max_clique = set()
    for k in interconnected:
        n1, n2, n3 = k
        clique = set([n1, n2, n3])
        if n1 in max_clique and n2 in max_clique and n3 in max_clique:
            continue
        for node in nodes:
            if node in clique:
                continue
            if all([node in graph[n] for n in clique]):
                clique.add(node)
        if len(clique) > max_clique_size:
            max_clique_size = len(clique)
            max_clique = set(clique)
    return ','.join(sorted(max_clique))


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