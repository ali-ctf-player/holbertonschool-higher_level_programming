#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    queens = []  # This will store [row, col] positions of queens

    def safe_position(row, col):
        # Check if new queen is safe from all existing queens
        for r, c in queens:
            # Same row or same diagonal?
            if r == row or abs(r - row) == abs(c - col):
                return False
        return True

    def solve(col):
        # If we placed queens in all columns, we found a solution
        if col == n:
            solutions.append(queens[:])  # Save a copy
            return

        # Try placing queen in each row of current column
        for row in range(n):
            if safe_position(row, col):
                queens.append([row, col])  # Place queen
                solve(col + 1)             # Move to next column
                queens.pop()               # Remove queen (backtrack)
    solve(0)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
