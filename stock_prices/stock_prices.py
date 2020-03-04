#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit_so_far = 0
  for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
      if (prices[j] - prices[i]) > max_profit_so_far:
        max_profit_so_far = prices[j] - prices[i]
  return max_profit_so_far


# print(find_max_profit([10, 20, 30, 40, 50, 60]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


# Understand
# input is a list of prices for stock 
# check the most possible profit between two prices
# the buy must come before the sell
# return the profit integer

# Plan
# for every number in the list, run a for loop on every following number to see what profit was made
# if the profit is lower than the maximum profit then replace it.
# return the max profit