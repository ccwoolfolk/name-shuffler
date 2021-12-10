import sys
from random import shuffle

assert len(sys.argv) == 2, 'No filename was provided'

filename = sys.argv[1]

with open(filename, 'r') as f:
    names = [l.strip() for l in f.readlines()]

shuffle(names)

for i, n in enumerate(names, 1):
    print(f'{i}: {n}')
