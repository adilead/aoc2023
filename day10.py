import os
import math
import re

def compute_loop(pipe_map):
  v = []
  e = {}
  s = None

  for y, row in enumerate(pipe_map):
    for x, pipe in enumerate(row):

      if pipe == ".":
        continue

      v.append((y, x))
      e[(y, x)] = []


      if pipe == "S":
        s = (y, x)
        if pipe_map[y+1][x] in ["L", "J", "|"]:
          e[(y, x)].append((y+1, x))
        if pipe_map[y-1][x] in ["F", "7", "|"]:
          e[(y, x)].append((y-1, x))
        if pipe_map[y][x-1] in ["F", "L", "-"]:
          e[(y, x)].append((y, x-1))
        if pipe_map[y][x+1] in ["7", "J", "-"]:
          e[(y, x)].append((y, x+1))

      elif pipe == "|":
        if pipe_map[y+1][x] in ["L", "J", "|", "S"]:
          e[(y, x)].append((y+1, x))
        if pipe_map[y-1][x] in ["F", "7", "|", "S"]:
          e[(y, x)].append((y-1, x))

      elif pipe == "-":
        if pipe_map[y][x-1] in ["F", "L", "-", "S"]:
          e[(y, x)].append((y, x-1))
        if pipe_map[y][x+1] in ["7", "J", "-", "S"]:
          e[(y, x)].append((y, x+1))

      elif pipe == "J":
        if pipe_map[y][x-1] in ["F", "L", "-", "S"]:
          e[(y, x)].append((y, x-1))
        if pipe_map[y-1][x] in ["F", "7", "|", "S"]:
          e[(y, x)].append((y-1, x))

      elif pipe == "F":
        if pipe_map[y+1][x] in ["L", "J", "|", "S"]:
          e[(y, x)].append((y+1, x))
        if pipe_map[y][x+1] in ["7", "J", "-", "S"]:
          e[(y, x)].append((y, x+1))

      elif pipe == "L":
        if pipe_map[y-1][x] in ["F", "7", "|", "S"]: 
          e[(y, x)].append((y-1, x))
        if pipe_map[y][x+1] in ["7", "J", "-", "S"]:
          e[(y, x)].append((y, x+1))

      elif pipe == "7":
        if pipe_map[y+1][x] in ["L", "J", "|", "S"]:
          e[(y, x)].append((y+1, x))
        if pipe_map[y][x-1] in ["F", "L", "-", "S"]:
          e[(y, x)].append((y, x-1))

  # visited = [False] * len(v)

  stack = [s]
  path = []
  # parent = {p: s for p in stack}
  parent = {}
  visited = set()
  while len(stack) != 0:
    x = stack.pop()
    visited.add(x)

    if x not in e:
      continue

    for n in e[x]:
      if n not in visited:
        stack.append(n)
        parent[n] = x

    for n in e[x]:
      if n == s and parent[x] != s:
        path.append(x)
        while parent[x] != s:
          path.append(parent[x])
          x = parent[x]
        path.append(s)
        return path

  return path

def part1(pipe_map):
  pipe_map = ["." + row.strip() + "." for row in pipe_map]
  pipe_map = ["".join(["."] * len(pipe_map[0]))] + pipe_map + ["".join(["."] * len(pipe_map[0]))]

  path = compute_loop(pipe_map)
  return int(math.ceil(len(path[:-1]) / 2))



def part2(pipe_map):
  pipe_map = ["." + row.strip() + "." for row in pipe_map]
  pipe_map = ["".join(["."] * len(pipe_map[0]))] + pipe_map + ["".join(["."] * len(pipe_map[0]))]

  path = compute_loop(pipe_map)
  # print("Path:")
  # print(path)
  path = set(path)
  markings = [[(y,x) in path for x,val in enumerate(row)] for y,row in enumerate(pipe_map)]

  # remove padding
  markings = markings[1:-1]
  markings = [row[1:-1] for row in markings]

  print("Markings:")
  for row in markings:
    print("".join(["x" if v else "." for v in row]))

  pipe_map = pipe_map[1:-1]
  pipe_map = [row[1:-1] for row in pipe_map]

  count = 0
  for y, row in enumerate(pipe_map):
    for x, pipe in enumerate(row):
      if markings[y][x]:
        continue

      a = [val if markings[y][p] is True and val == "|" else "x" for p, val in enumerate(row[:x])]
      b = [val if markings[y][x+1+p] is True and val == "|" else "x" for p, val in enumerate(row[x+1:])]
      c = [val if markings[p][x] is True and val == "-" else "x" for p, val in enumerate([pipe_map[i][x] for i in range(0, y)])]
      d = [val if markings[y+1+p][x] is True and val == "-" else "x" for p, val in enumerate([pipe_map[i][x] for i in range(y+1, len(pipe_map))])]

      a += ["|" for v in re.findall(r"L-*7|F-*J", row[:x])]
      b += ["|" for v in re.findall(r"L-*7|F-*J", row[x+1:])]
      c += ["-" for v in re.findall(r"F\|*J|7\|*L", "".join([pipe_map[i][x] for i in range(0, y)]))]
      d += ["-" for v in re.findall(r"F\|*J|7\|*L", "".join([pipe_map[i][x] for i in range(y+1, len(pipe_map))]))]

      if a.count("|") % 2 != 0 and b.count("|") % 2 != 0 and c.count("-") % 2 != 0 and d.count("-") % 2 != 0:
        count += 1
        pipe_map[y] = pipe_map[y][:x] + "I" + pipe_map[y][x+1:]
        # print((y,x))
        # print(a)
        # print(b)
        # print(c)
        # print(d)

  [print(row) for row in pipe_map]
  return count



if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test2.txt", "test3.txt", "input.txt"]
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
