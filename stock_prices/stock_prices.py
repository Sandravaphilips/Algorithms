#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # loop through each price from the start to end-1
  # save that as the cost price
  # loop through each price following it until end
  # subtract the cost price from each selling price
  # return the maximum value
  index = 0
  profit = []
  
  while index < len(prices)-1:
    sales_prices = prices[index+1:]
    for i in sales_prices:
      profit.append(i-prices[index])
    index += 1

  return max(profit)
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))