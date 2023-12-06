import re
import sys
import os
import math

def part1(data):
  data = [line.strip().split(":")[1] for line in data]
  data = [[int(val) for val in re.findall(r"\d+", line)] for line in data]
  games = list(zip(*data))

  val = 1
  for time, dist in games:
    count = 0
    for load in range(0, time+1):
      diff = time - load
      d = diff * load
      if d > dist:
        count += 1
    val *= count
  return val


def part2(data):
  data = [line.strip().split(":")[1] for line in data]
  data = [int("".join(re.findall(r"\d+", line))) for line in data]
  time, dist = data

  a_1 = (-time + math.sqrt(time ** 2 - 4 * dist)) / -2
  a_2 = (-time - math.sqrt(time ** 2 - 4 * dist)) / -2

  num = abs(a_1 - a_2)

  return int(num)


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

