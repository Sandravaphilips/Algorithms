#!/usr/bin/python

import sys
from itertools import product

def rock_paper_scissors(n):
  number_of_plays = []
  for i in list(product(['rock', 'paper', 'scissors'], repeat=n)):
    number_of_plays.append(list(i))
  return number_of_plays 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print(rock_paper_scissors(2))