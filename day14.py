import re
import sys
import os
import time
import numpy as np

def part1(dish):
  dish = [line.strip() for line in dish]

  # add padding and change strings to list for easier manipulation
  dish = [list("#" + row.strip() + "#") for row in dish]
  dish = [["#"] * len(dish[0])] + dish + [["#"] * len(dish[0])]

  rocks = [(y,x) for y, row in enumerate(dish) for x, el in enumerate(row) if el == "O"]
  stops = {(y,x):[] for y, row in enumerate(dish) for x, el in enumerate(row) if el == "#"}
  for stop in stops:
    y,x = stop
    while dish[y][x] != "#":
      if dish[y][x] == "O":
        stops[stop].append((y,x))
        y += 1



  new_dish = [[el for el in row] for row in dish]
  np.array(new_dish)
  changed = True
  start = time.perf_counter()
  its = 0
  while changed:
    changed = False
    for i,rock in enumerate(rocks):
      y,x = rock
      if new_dish[y-1][x] == ".":
        changed = True
        new_dish[y-1][x] = "O"
        new_dish[y][x] = "."
        rocks[i] = (y-1,x)
      else:
        rocks[i] = (y,x)
    # rocks.sort(key= lambda x: x[0])
    rocks = [(y,x) for y, row in enumerate(new_dish) for x, el in enumerate(row) if el == "O"]
    # print(rocks)
    its += 1

  end = time.perf_counter()
  print(f"Took {end -start}s for {its} iterations")
  sum = 0
  # for y,line in enumerate(dish[1:-1]):
  #   sum += line.count("O") * (len(dish)-2-y)
  for rock in rocks:
    sum += (len(dish)-1-rock[0])
  
  return sum
    
def part2(dish):
  dish = [line.strip() for line in dish]

  # add padding and change strings to list for easier manipulation
  dish = [list("#" + row.strip() + "#") for row in dish]
  dish = [["#"] * len(dish[0])] + dish + [["#"] * len(dish[0])]

  def rotate(dish):
    rot_dish = ['.' * len(dish) for _ in dish[0]]
    for c_i in range(len(dish[0])):
      new_row = ''.join([row[c_i] for row in dish][::-1])
      rot_dish[c_i] = new_row

    return rot_dish
  
  now = time.perf_counter()
  orig_dish = dish
  last_dishes = []
  final_idx = -1
  for i in range(1_000_000_000):
    for rot in range(4):
      # Move rocks to north
      cols = []
      for c_i in range(len(dish[0])):
        col = [row[c_i] for row in dish]
        l = len(col)
        for a in range(l):
          if col[a] == 'O':
            for b in range(a-1, 0, -1):
              if col[b] == "." and col[b-1] in ["O", "#"]:
                col[b] = "O"
                col[a] = "."
              elif col[b] in ["O", "#"]:
                break
        cols.append(col)
      # transpose back
      for c_i in range(len(cols)):
        dish[c_i] = ''.join([col[c_i] for col in cols])

      dish = rotate(dish)

      # we are only interested in north rotations
      if rot != 3: continue

      # cache north orientations
      cached_dish = dish
      cached_dish = ''.join([row for row in cached_dish])


      # we search for cached dishes
      found = None
      found_id = -1
      for i_d, ld in enumerate(last_dishes):
        if ld == cached_dish:
          found = ld
          found_id = i_d 
          break
      last_dishes.append(cached_dish)


      if found is not None:
        print(f"Found dish at {found_id} on iteration {i}")
        start = found_id
        delta = i - start
        x = (1_000_000_000 - 1 - start ) % delta
        final_idx = start + x
        break
    if final_idx != -1:
      break

    if i % 1000 == 0:
      print(i)
  
  final_dish = last_dishes[final_idx]
  final_dish = [''.join(final_dish[k:k+len(orig_dish[0])]) for k in range(0, len(final_dish), len(orig_dish[0]))]

  # compute weight on northern support beam
  sum = 0
  for y, row in enumerate(final_dish[1:-1]):
    sum += (len(final_dish)-2-y) * row.count("O")
  print(f"Took {time.perf_counter() - now:.2f}s")
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
