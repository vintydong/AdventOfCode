import pathlib
import sys

def parse(puzzle_input):
    """Parse puzzle"""
    levels = puzzle_input.split("\n")
    return levels

def check_safe_report(report):
    increasing = int(report[1]) > int(report[0])
    for i,level in enumerate(report[1:]):
        prev = int(report[i])
        level = int(level)
        diff = abs(level - prev)
        if increasing and level <= prev or not increasing and level >= prev or diff > 3:
            return i + 1
    return -1

def part1(data):
    """Solve part 1."""
    count = 0
    for report in data:
        report = report.split(' ')
        if check_safe_report(report) == -1:
            count += 1
    return count

def part2(data):
    """Solve part 2."""
    count = 0
    unsafe_reports = []
    for report in data:
        report = report.split(' ')
        res = check_safe_report(report)
        if res == -1:
            count += 1
        else:
            unsafe_reports.append(report)

    for report in unsafe_reports:
        for i in range(len(report)):
            modified = report[:i] + report[i+1:]
            if check_safe_report(modified) == -1:
                count += 1
                break
    return count

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