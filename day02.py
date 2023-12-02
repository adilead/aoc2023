import os
import math
import re

def part1(input_lines):
  max_col = {
    "red": 12,
    "green": 13,
    "blue": 14,
  }

  games = [re.split(",|;", line.split(":")[1]) for line in input_lines]
  sum = 0
  for i, game in enumerate(games):
    for gset in game:
      num, col = gset.strip().split(" ")
      add = True
      if int(num) > max_col[col]:
        add = False
        break
    if add:
      sum += i+1
  return sum


def part2(input_lines):
  games = [re.split(",|;", line.split(":")[1]) for line in input_lines]
  sum = 0
  for game in games:
    max_col = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }
    for gset in game:
      num, col = gset.strip().split(" ")
      if int(num) > max_col[col]:
        max_col[col] = int(num)
    sum += math.prod(max_col.values())
  return sum


if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test.txt", "input.txt"]
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
