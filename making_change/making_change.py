#!/usr/bin/python

import sys

def making_change(amount, denominations):
  changes = [1]+[0]*amount

  for i in denominations:
    for j in range(i,amount+1):
      changes[j] += changes[j-i]
    
  return changes[amount]
  


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print(making_change(20, [1, 5, 10, 25, 50]))