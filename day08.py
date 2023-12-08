import re
import math
import os
from functools import reduce


def part1(input_lines):
  directions = input_lines[0].strip()
  nodes = [line.strip() for line in input_lines[2:]]
  nodes = [re.findall(r"[A-Z]{3}", line) for line in nodes]
  nodes = {line[0]: line[1:] for line in nodes}

  counter = 0
  zzz_not_found = True
  curr_node = "AAA"
  while zzz_not_found:
    for d in directions:
      if d == "L":
        curr_node = nodes[curr_node][0]
      elif d == "R":
        curr_node = nodes[curr_node][1]
      counter += 1
      zzz_not_found = curr_node != "ZZZ"
      if not zzz_not_found:  # it was found
        break
  return counter


def part2(input_lines):
  directions = input_lines[0].strip()
  input_lines = [line.strip() for line in input_lines[2:]]
  input_lines = [re.findall(r"\w{3}", line) for line in input_lines]
  nodes = {line[0]: line[1:] for line in input_lines}

  curr_nodes = [line[0] for line in input_lines if line[0][-1] == "A"]

  first_hit = []
  for curr_node in curr_nodes:
    counter = 0
    zzz_found = False
    while not zzz_found:
      for d in directions:
        if d == "L":
          curr_node = nodes[curr_node][0]
        elif d == "R":
          curr_node = nodes[curr_node][1]
        counter += 1
        zzz_found = curr_node[-1] == "Z"
        if zzz_found:  # it was found
          first_hit.append(counter)
          break

  return math.lcm(*first_hit)


if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test1.txt", "test2.txt", "input.txt"]
  inputs_2 = ["test3.txt", "input.txt"]
  # inputs_2 = ["input.txt"]

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
