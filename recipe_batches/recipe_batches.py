#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_values = list(recipe.values())
  ingredients_values = list(ingredients.values())
  index = 0
  multiples_of_values = []
  dif_in_length = len(recipe_values) - len(ingredients_values)
  extension = [0] * dif_in_length
  
  if dif_in_length > 0:
    ingredients_values.extend(extension)
  elif dif_in_length < 0:
    recipe_values.extend(extension)

  while index < len(recipe_values):
    multiples = int(ingredients_values[index] / recipe_values[index])
    multiples_of_values.append(multiples)
    index += 1

  return min(multiples_of_values)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients =  { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))