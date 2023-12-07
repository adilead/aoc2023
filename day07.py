import re
import sys
import os
import functools
from math import prod

def card_bigger(c1, c2):
  cards = "AKQJT98765432"
  # true if c1 bigger than c2
  i1 = cards.find(c1)
  i2 = cards.find(c2)
  return i1 < i2

def compute_hand(hand):
  if hand == len(hand) * hand[0]:
    return "5k"
  elif len(set(hand)) == 2:
    if hand.count(hand[0]) in [1, 4]:
      return "4k"
    else:
      return "fh"
  elif len(set(hand)) == 3:
    if any([hand.count(h) == 3 for h in hand]):
      return "3k"
    else:
      return "2p"
  elif len(set(hand)) == 4:
    return "1p"
  else:
    return "hc"

def compare_hands(a, b):
  cards = ["5k", "4k", "fh", "3k", "2p", "1p", "hc"]
  i1 = cards.index(compute_hand(a))
  i2 = cards.index(compute_hand(b))
  if i1 < i2:  # a > b
    return 1
  elif i2 < i1:  # a < b
    return -1

  # hands are equal
  for c1, c2 in zip(a, b):
    if c1 == c2:
      continue
    else:
      if card_bigger(c1, c2):
        return 1
      else:
        return -1

  # I don't assume that this will be reached
  return 0


def part1(lines):
  hands, bids = zip(*[line.strip().split(" ") for line in lines])
  hands_bids = {hand: int(bids[i]) for i, hand in enumerate(hands)}
  hands = list(hands)

  hands_sorted = sorted(hands, key=functools.cmp_to_key(compare_hands))

  value = sum([hands_bids[hand] * (i+1) for i, hand in enumerate(hands_sorted)])
  return value


# ==================================================================

def card_bigger_2(c1, c2):
  cards = "AKQT98765432J"
  # true if c1 bigger than c2
  i1 = cards.find(c1)
  i2 = cards.find(c2)
  return i1 < i2

def compute_hand_2(hand):
  if "J" not in hand:
    return compute_hand(hand)

  j_count = hand.count("J")
  hand = "".join(hand.split("J"))
  if len(set(hand)) <= 1:
    return "5k"
  elif len(set(hand)) == 2:
    if any([hand.count(h) + j_count == 4 for h in hand]):
      return "4k"
    else:
      return "fh"
  elif len(set(hand)) == 3:
    if any([hand.count(h) + j_count == 3 for h in hand]):
      return "3k"
    else:
      return "2p"
  elif len(set(hand)) == 4:
    return "1p"
  else:
    return None

def compare_hands_2(a, b):
  cards = ["5k", "4k", "fh", "3k", "2p", "1p", "hc"]
  i1 = cards.index(compute_hand_2(a))
  i2 = cards.index(compute_hand_2(b))
  if i1 < i2:  # a > b
    return 1
  elif i2 < i1:  # a < b
    return -1

  # hands are equal
  for c1, c2 in zip(a, b):
    if c1 == c2:
      continue
    else:
      if card_bigger_2(c1, c2):
        return 1
      else:
        return -1

  # I don't assume that this will be reached
  return 0

def part2(lines):
  hands, bids = zip(*[line.strip().split(" ") for line in lines])
  hands_bids = {hand: int(bids[i]) for i, hand in enumerate(hands)}
  hands = list(hands)

  hands_sorted = sorted(hands, key=functools.cmp_to_key(compare_hands_2))

  value = sum([hands_bids[hand] * (i+1) for i, hand in enumerate(hands_sorted)])
  return value


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
