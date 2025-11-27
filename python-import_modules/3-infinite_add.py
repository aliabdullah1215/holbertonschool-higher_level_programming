#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    total = 0

    for num in args:
        total += int(num)

    print(total)
