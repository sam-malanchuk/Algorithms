#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache):
  # check if the n has already been calculate
  if cache and n in cache:
    return n
  
  # base case, he cannot eat anymore cookies
  if n == 0:
    return 1
  
  total_ways = 0
  if n >= 3:
    # eat all the cookies
    total_ways += eating_cookies(n-3, cache)
    # save the result of n-3 into cache for reuse
    cache[n-3] = total_ways
  if n >= 2:
    # eat 2 cookies
    total_ways += eating_cookies(n-2, cache)
    cache[n-2] = total_ways
  if n >= 1:
    # eat 1 cookie
    total_ways += eating_cookies(n-1, cache)
    cache[n-1] = total_ways
  return total_ways


# print(eating_cookies(30, {}))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# Understand
# Take a number of cookies 'n' and calculate all the possible ways 3, 2, and 1 can go into it.
# If 'n' is 0 then return 0

# Plan
# 