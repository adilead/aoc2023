import re
import sys
import os

def part1(schematic):
  # pad
  schematic = ['.' * len(schematic[0])] + schematic + ['.' * len(schematic[0])]
  schematic = ['.' + line.strip() + '.' for line in schematic]

  numbers = "0123456789"
  pos = []
  for y, row in enumerate(schematic):
    if y == 0 or y == len(schematic)-1:
      continue
    for x, val in enumerate(row):
      if x == 0 or x == len(row)-1:
        continue
      if val not in numbers and val != '.':
        if schematic[y-1][x] in numbers:
          pos.append((y-1, x))
        if schematic[y+1][x] in numbers:
          pos.append((y+1, x))
        if schematic[y][x-1] in numbers:
          pos.append((y, x-1))
        if schematic[y][x+1] in numbers:
          pos.append((y, x+1))
        if schematic[y-1][x+1] in numbers:
          pos.append((y-1, x+1))
        if schematic[y+1][x+1] in numbers:
          pos.append((y+1, x+1))
        if schematic[y-1][x-1] in numbers:
          pos.append((y-1, x-1))
        if schematic[y+1][x-1] in numbers:
          pos.append((y+1, x-1))
  r = re.compile("\d+")
  sum = 0
  added = []
  for y, x in pos:
    for m in r.finditer("".join(schematic[y])):
      if (m.start(), y) not in added and m.start() <= x < m.start() + len(m.group()):
        sum += int(m.group())
        added.append((int(m.start()), y))
  return sum


def part2(schematic):
  # pad
  schematic = ['.' * len(schematic[0])] + schematic + ['.' * len(schematic[0])]
  schematic = ['.' + line.strip() + '.' for line in schematic]

  numbers = "0123456789"
  pos = []
  for y, row in enumerate(schematic):
    if y == 0 or y == len(schematic)-1:
      continue
    for x, val in enumerate(row):
      if x == 0 or x == len(row)-1:
        continue
      temp = []
      if val == '*':
        if schematic[y-1][x] in numbers:
          temp.append((y-1, x))
        else:
          if schematic[y-1][x+1] in numbers:
            temp.append((y-1, x+1))
          if schematic[y-1][x-1] in numbers:
            temp.append((y-1, x-1))

        if schematic[y+1][x] in numbers:
          temp.append((y+1, x))
        else:
          if schematic[y+1][x+1] in numbers:
            temp.append((y+1, x+1))
          if schematic[y+1][x-1] in numbers:
            temp.append((y+1, x-1))

        if schematic[y][x-1] in numbers:
          temp.append((y, x-1))
        if schematic[y][x+1] in numbers:
          temp.append((y, x+1))

      if len(temp) == 2:
        pos.append(temp)
  r = re.compile("\d+")
  sum = 0
  a, b = 0, 0
  for (y_1, x_1), (y_2, x_2) in pos:
    for m in r.finditer(schematic[y_1]):
      if m.start() <= x_1 < m.start() + len(m.group()):
        a = int(m.group())
        break
    for m in r.finditer(schematic[y_2]):
      if m.start() <= x_2 < m.start() + len(m.group()):
        b = int(m.group())
        break
    sum += a * b
  return sum


if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test.txt", "input.txt", ]
  inputs_2 = ["test.txt", "input.txt"]

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
