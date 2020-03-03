# !/usr/bin/python

import argparse

def find_max_profit(prices):
  pass

print(find_max_profit([100, 90, 80, 50, 20, 10]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


# Understand
# input is a list of prices for stock 
# check the most possible profit between two prices
# the buy must come before the sell
# return the profit integer

# Plan
# for every number in the list, run a for loop on every following number to see what profit was made
# if the profit is lower than the maximum profit then replace it.
# return the max profit