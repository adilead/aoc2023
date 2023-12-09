import re
import sys
import os

def part1(input_lines):
  seqs = [[int(val) for val in re.findall(r"-?\d+", line)] for line in input_lines]

  s = 0
  for seq in seqs:
    sub_seqs = []
    curr_seq = seq
    sub_seqs.append(curr_seq)
    while not all(v == curr_seq[0] for v in curr_seq):
      curr_seq = [j-i for i, j in zip(curr_seq[:-1], curr_seq[1:])]
      sub_seqs.append(curr_seq)

    y = [seq[-1] for seq in sub_seqs]
    s += sum(y)
  return s


def part2(input_lines):
  seqs = [[int(val) for val in re.findall(r"-?\d+", line)] for line in input_lines]

  s = 0
  for seq in seqs:
    sub_seqs = []
    curr_seq = seq
    sub_seqs.append(curr_seq)
    while not all(v == curr_seq[0] for v in curr_seq):
      curr_seq = [j-i for i, j in zip(curr_seq[:-1], curr_seq[1:])]
      sub_seqs.append(curr_seq)

    v = sub_seqs[-1][0]
    for seq in reversed(sub_seqs[:-1]):
      v = seq[0] - v
    s += v
  return s


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
