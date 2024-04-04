import os
from collections import deque
from sre_constants import ATCODES

def asciihash(str):
  s = 0
  for c in str:
    s = s + ord(c)
    s = (s*17) % 256
  return s

def part1(inp):
  seq = ','.join([line.strip() for line in inp]).split(",")
  sum = 0
  for ini in seq:
       sum += asciihash(ini)
  return sum


def part2(inp):
  seq = ','.join([line.strip() for line in inp]).split(",")
  boxes_labels = [deque() for i in range(256)]
  boxes_foc = [deque() for i in range(256)]
  for ini in seq:
    if "-" in ini:
      label, _ = ini.split("-") 
      h = asciihash(label)
      if label in boxes_labels[h]:
        idx = boxes_labels[h].index(label)
        boxes_labels[h].remove(label)
        del boxes_foc[h][idx]
    elif "=" in ini:
      label, foc = ini.split("=") 
      h = asciihash(label)
      if label in boxes_labels[h]:
        label_idx = boxes_labels[h].index(label)
        boxes_labels[h][label_idx] = label
        boxes_foc[h][label_idx] = foc
      else:
        boxes_labels[h].append(label)
        boxes_foc[h].append(foc)
  
  val = 0
  for h, box_label in enumerate(boxes_labels):
    for i,foc in enumerate(boxes_foc[h]):
      s = (h+1)*(i+1)*int(foc)
      val = val + s  
  return val


if __name__ == "__main__":
  day = os.path.basename(__file__).split(".")[0]
  root = os.path.dirname(__file__)
  input_dir = os.path.join(root, "inputs", day)
  inputs_1 = ["input.txt"]
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
