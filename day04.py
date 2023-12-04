import re
import sys
import os

def part1(card):
  card = [re.split(r":|\|", line.strip())[1:] for line in card]
  card = [[set(re.findall(r"\d+", nums)) for nums in line] for line in card]
  sum = 0
  for line in card:
    matches = line[0].intersection(line[1])
    sum += 2 ** (len(matches) - 1) if len(matches) >= 1 else 0
  return sum


def part2(cards):
  cards = [re.split(r":|\|", line.strip()) for line in cards]
  cards = [[re.findall(r"\d+", nums) for nums in line] for line in cards]
  matches = [len(set(line[1]).intersection(set(line[2]))) for line in cards]
  copies = [1 for line in cards]
  for i,m in enumerate(matches):
    copies = copies[:i+1] + [c+copies[i] for c in copies[i+1:i+1+m]] + copies[i+1+m:]
  return sum(copies)



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
