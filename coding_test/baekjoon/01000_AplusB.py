import sys

if __name__ == "__main__":
    lines = sys.stdin.readlines()

    for line in lines:
        line = line.strip()
        a, b = line.split(" ")
        print(int(a) + int(b))
