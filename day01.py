import re
import os

def part1(input_lines):
  sum = 0
  for line in input_lines:
    digits = re.findall(r'\d', line)
    if len(digits) < 1:
      continue
    sum += int(digits[0] + digits[-1])
  return sum


def part2(input_lines):
  digits = ["null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  sum = 0
  for line in input_lines:
    min_pos, max_pos = len(line), 0
    min_digit, max_digit = '', ''
    for i, digit in enumerate(digits):

      pos = line.find(digit)
      if pos != -1 and min_pos > pos:
        min_pos = pos
        min_digit = str(i)

      pos = line.rfind(digit)
      if pos != -1 and max_pos < pos:
        max_pos = pos
        max_digit = str(i)

    for c_i, c in enumerate(line):
      if c not in "1234567890":
        continue
      if c_i < min_pos:
        min_digit = c
        break

    for c_i, c in enumerate(reversed(line)):
      if c not in "1234567890":
        continue
      if len(line) - c_i > max_pos:
        max_digit = c
        break

    sum += int(min_digit+max_digit)
  return sum


if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["test_1.txt", "input.txt"]
  inputs_2 = ["test_2.txt", "input.txt"]

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

