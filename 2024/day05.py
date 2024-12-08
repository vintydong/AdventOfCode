import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    lines = puzzle_input.split('\n')
    page_ordering = {}
    updates = []
    for line in lines:
        if '|' in line:
            a,b = line.split('|')
            if a in page_ordering:
                page_ordering[a].add(b)
            else:
                page_ordering[a] = set([b])
        elif line.strip() != '':
            updates.append(line.split(','))
    return page_ordering, updates

def part1(data):
    """Solve part 1."""
    page_ordering, updates = data
    s = 0
    for pages in updates:
        ordered = True
        for i in range(len(pages)):
            before_pages = pages[:i]
            for bp in before_pages:
                if pages[i] in page_ordering and bp in page_ordering[pages[i]]:
                    ordered = False
                    break
            if not ordered:
                # print("False", pages)
                break
        else:
            s += int(pages[len(pages)//2])
    return s

def get_unordered(data):
    page_ordering, updates = data
    unordered = []
    for pages in updates:
        ordered = True
        for i in range(len(pages)):
            before_pages = pages[:i]
            for bp in before_pages:
                if pages[i] in page_ordering and bp in page_ordering[pages[i]]:
                    ordered = False
                    break
            if not ordered:
                break
        else:
            continue
        unordered.append(pages)
    return unordered

def topological_sort(nodes, edges):
    def has_incoming_edge(node):
        for node_edges in edges.values():
            if node in node_edges:
                return True
        return False
    no_incoming = []
    # inefficient checking of incoming edges
    for node in nodes:
        if not has_incoming_edge(node):
            no_incoming.append(node)

    sorted_list = []
    while len(no_incoming) > 0:
        node = no_incoming.pop()
        sorted_list.append(node)
        if node in edges:
            removed_edges = edges.pop(node)
        else:
            removed_edges = []
        for n in removed_edges:
            if not has_incoming_edge(n) and n in nodes:
                no_incoming.append(n)
    
    return sorted_list

def part2(data):
    """Solve part 2."""
    page_ordering, updates = data
    unordered_updates = get_unordered(data)
    s = 0
    for update in unordered_updates:
        nodes = update
        out_edges = {page: page_ordering.get(page, []) for page in update}
        sorted_list = topological_sort(nodes, out_edges)
        s += int(sorted_list[len(sorted_list) // 2])
    return s

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