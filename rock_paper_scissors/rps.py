# !/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  sets = []
  for rock in range(n):
    for paper in range(n):
      for scissors in range(n):
        sets.append([rps[rock], rps[paper], rps[scissors]])
  return sets

print(rock_paper_scissors(3))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')

# Understand
# 