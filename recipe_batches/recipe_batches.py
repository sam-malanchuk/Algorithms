# !/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = 0
  for key, ingredient in ingredients.items():
    if ingredient == 0:
      return 0
    print(recipe[key])
  return max_batches

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
print(recipe_batches(recipe, ingredients))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# Understand
# Check the ingredient for every item in the recipe if there is enough
# return the total number of times you could make the recipe.

# Plan
# Keep track of the max batches starting from 0
# divide the ingredient needed for the recipe by the ingredient we have
# if throw away the left over recording how many you can make
# keep the lowest about you can make from the ingredients in the max batch variable
# if there is 0 of any ingredient, immediately return 0