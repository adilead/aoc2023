import re
import sys
import os

def part1(input_lines):
  input_lines = [line.strip() for line in input_lines]
  rows = [line.count("#") == 0 for line in input_lines]
  cols = ["".join([v[i] for v in input_lines]).count("#") == 0 for i in range(len(input_lines[0]))]
  galaxies = []
  for i,r in enumerate(rows):
    galaxies.append(input_lines[i])
    if r:
      galaxies.append(input_lines[i])

  offset = 0
  for i, c in enumerate(cols):
    if c:
      galaxies = [row[:i+offset+1] + "." + row[i+offset+1:] for row in galaxies]
      offset += 1
  
  gals = [[(y,x) for x,v in enumerate(row) if v == "#"] for y, row in enumerate(galaxies)]
  gals = [g for row in gals for g in row]

  found = set()
  sum = 0
  for g1 in gals:
    for g2 in gals:
      if g1 != g2 and (g1, g2) not in found:
        dist = abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        sum += dist
        found.add((g1, g2))
        found.add((g2, g1))

  return sum

  


def part2(input_lines):
  f = 1_000_000
  input_lines = [line.strip() for line in input_lines]
  rows = [f if line.count("#") == 0 else 1 for line in input_lines]
  cols = [f if "".join([v[i] for v in input_lines]).count("#") == 0 else 1 for i in range(len(input_lines[0]))]

  gals = [[(y,x) for x,v in enumerate(row) if v == "#"] for y, row in enumerate(input_lines)]
  gals = [g for row in gals for g in row]

  found = set()
  acc = 0
  for g1 in gals:
    for g2 in gals:
      if g1 != g2 and (g1, g2) not in found:
        rs = rows[g1[0]+1:g2[0]+1] if g1[0] < g2[0] else rows[g2[0]+1:g1[0]+1]
        cs = cols[g1[1]+1:g2[1]+1] if g1[1] < g2[1] else cols[g2[1]+1:g1[1]+1]
        dist = sum(rs) + sum(cs)
        acc += dist
        found.add((g1, g2))
        found.add((g2, g1))

  return acc



if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test1.txt", "input.txt"]
  inputs_2 = ["input.txt"]

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
