import re
import sys
import os

from collections import deque


def find_vertical(pattern):
  cols = ["".join(l) for l in zip(*[list(s) for s in pattern])]
  stack = deque()
  stack.append(cols[0])
  for border,col in enumerate(cols[1:]):
    check = stack.copy()
    rest = cols[border+1:]
    for i, c in enumerate(rest):
      if c == check[-1]:
        check.pop()
        if len(check) == 0 or i == len(rest)-1:
          return border+1
      else:
        break
    stack.append(col)

  return 0

def part1(lines):
  patterns = [[]]
  for line in lines:
    if len(line.strip()) == 0:
      patterns.append([])
      continue
    patterns[-1].append(line.strip())

  sum = 0
  for pattern in patterns:
    v = find_vertical(pattern)
    transposed = ["".join(l) for l in zip(*[list(s) for s in pattern])]
    h = 100*find_vertical(transposed)
    sum += v + h
  return sum


def find_vertical_smudged(pattern):
  # old_border = find_vertical(pattern)-1
  cols = ["".join(l) for l in zip(*[list(s) for s in pattern])]
  for border,col in enumerate(cols[:-1]):
    left, right = cols[:border+1], cols[border+1:]
    right = list(reversed(right))
    diff = abs(len(right) - len(left))
    if len(right) > len(left):
      right = right[diff:]
    elif len(right) < len(left):
      left = left[diff:]

    x = [c for l in left for c in l]
    for i in range(len(x)):
      x[i] = "#" if x[i] == "." else "."
      test = ["".join(x[k:k + len(left[0])]) for k in range(0, len(x), len(left[0]))]
      if all([test[k] == right[k] for k in range(len(right))]):
        return border+1
      x[i] = "#" if x[i] == "." else "."
  return 0


def part2(lines):
  patterns = [[]]
  for line in lines:
    if len(line.strip()) == 0:
      patterns.append([])
      continue
    patterns[-1].append(line.strip())

  sum = 0
  for pattern in patterns:
    v = find_vertical_smudged(pattern)
    transposed = ["".join(l) for l in zip(*[list(s) for s in pattern])]
    print("---")
    h = 100*find_vertical_smudged(transposed)
    print(v,h)
    sum += v + h
  return sum



if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test.txt", "input.txt"]
  inputs_2 = ["test.txt","input.txt"]

  print("==== Results part 1 ====")
  for input in inputs_1:
    with open(os.path.join(input_dir, input), "r") as f:
      input_content = f.readlines()
    result = part1(input_content)
    print(f"{input}: {result}")

  print("==== Results part 2 ====")
  for input in inputs_2:
    with open(os.path.join(input_dir, input), "r") as f:
      input_content = f.readlines()
    result = part2(input_content)
    print(f"{input}: {result}")
