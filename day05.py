import re
import sys
import os
import math

from typing import List

import numba as nb
from numba.typed import List

def part1(almanac):
  seeds = []
  maps = {}
  curr_map = -1
  for line in almanac:
    if line == '\n':
      continue
    elements = line.strip().split(" ")
    if 'seeds' in elements[0]:
      seeds = [int(el) for el in elements[1:]]
    elif not elements[0][0].isdigit():
      curr_map += 1
      maps[curr_map] = []
    else:
      maps[curr_map].append([int(el) for el in elements])

  def convert(s, map):
    for m in map:
      if s - m[1] > 0 and s - m[1] < m[2]:
        return s - m[1] + m[0]
    return s

  for i in range(0, curr_map+1):
    seeds = [convert(s, maps[i]) for s in seeds]
  return min(seeds)

def convert(s, map):
  for m in map:
    if s - m[1] >= 0 and s - m[1] < m[2]:
      return s - m[1] + m[0]
  return s

@nb.jit(nopython=True)
def brute(start: int, end: int, maps):
  min_loc = 2**32
  for seed in range(start, end):
    for i,map in enumerate(maps):
      c = seed
      for m in map:
        if seed - m[1] >= 0 and seed - m[1] < m[2]:
          c = seed - m[1] + m[0]
          break
      seed = c
    if seed < min_loc:
      min_loc = seed
  return min_loc


def part2(almanac):
  seeds = []
  maps = []
  curr_map = -1
  for line in almanac:
    if line == '\n':
      continue
    elements = line.strip().split(" ")
    if 'seeds' in elements[0]:
      seeds = [int(el) for el in elements[1:]]
    elif not elements[0][0].isdigit():
      curr_map += 1
      maps.append([])
    else:
      maps[-1].append([int(el) for el in elements])

  # maps = List([List([List(x) for x in y]) for y in maps])

  # seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

  # min_seed = math.inf
  # for s in seeds:
  #   print(s)
  #   s = brute(s[0], s[0]+s[1], maps)
  #   if s < min_seed:
  #     min_seed = s
  # TODO Brute force doesnt work, FIXME
  return -1



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
