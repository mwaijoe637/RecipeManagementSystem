from lib.helpers import *

def display_menu():
  print('Menu:')
  print('1. Create Ingredient')
  print('2. List Ingredients')
  print('3. Update Ingredient')
  print('4. Delete Ingredient')
  print('5. Create Recipe')
  print('6. List Recipes')
  print('7. Update Recipe')
  print('8. Delete Recipe')
  print('9. Search Recipe')
  print('10. Exit')

def handle_option(option):
  if option == 1:
    name = input('Enter Ingredient Name: ')
    Ingredients.create_ingredient(name)
  elif option == 2:
    Ingredients.read_ingredients()
  elif option == 3:
    Ingredients.read_ingredients()
    try:
      id = int(input('Enter the Ingredient ID to update: '))
    except ValueError:
      print('Invalid Input. Please Enter a Number.')
    name = input('Enter the New Ingredient name: ')
    Ingredients.update_ingredient(id, name)
  elif option == 4:
    Ingredients.read_ingredients()
    try:
      id = int(input('Enter the Ingredient ID to delete: '))
    except ValueError:
      print('Invalid Input. Please Enter a Number.')
    Ingredients.delete_ingredient(id)
  elif option == 5:
    name = input('Enter Recipe Name: ')
    description = input('Enter Recipe Description: ')
    cuisine = input('Enter Recipe Cuisine: ')
    dietary = input('Enter Recipe Dietary: ')
    Recipes.create_recipe(name, description, cuisine, dietary)
  elif option == 6:
    Recipes.read_recipes()
    print('\nActions')
    print('1. View Recipe Details')
    print('2. Back To Main Menu')
    choice = int(input('Enter your choice: '))
    if choice == 1:
      recipe_id = int(input('Enter Recipe ID To View Details: '))
      Recipes.read_recipe_info(recipe_id)
      print('\nActions')
      print('1. Add Ingredient To Recipe')
      print('2. Remove Ingredient From Recipe')
      print('3. Back To Main Menu')
      choice = int(input('Enter your choice: '))
      if choice == 1:
        Ingredients.read_ingredients()
        ingredient_id = int(input('Enter Ingredient ID To Add To This Recipe: '))
        RecipeIngredients.create(ingredient_id, recipe_id)
        Recipes.read_recipe_info(recipe_id)
        main()
      elif choice == 2:
        Ingredients.read_ingredients()
        ingredient_id = int(input('Enter Ingredient ID To Remove From This Recipe: '))
        RecipeIngredients.delete(ingredient_id, recipe_id)
        Recipes.read_recipe_info(recipe_id)
        main()
      elif choice == 3:
        main()
      else:
        print('Invalid Option. Taking You To Main Menu.')
        main()
    elif choice == 2:
      main()
    else:
      print('Invalid Option. Taking You To Main Menu.')
      main()
  elif option == 7:
    Recipes.read_recipes()
    try:
      id = int(input('Enter the Recipe ID to update: '))
    except ValueError:
      print('Invalid Input. Please Enter a Number.')
    print('Enter New Details Below. Leave Blank if You Dont wish to Update.\n')
    name = input('Enter New Recipe Name: ')
    description = input('Enter New Recipe Description: ')
    cuisine = input('Enter New Recipe Cuisine: ')
    dietary = input('Enter New Recipe Dietary: ')
    Recipes.update_recipe(id, name, description, cuisine, dietary)
  elif option == 8:
    Recipes.read_recipes()
    try:
      id = int(input('Enter the Recipe ID to delete: '))
    except ValueError:
      print('Invalid Input. Please Enter a Number.')
    Recipes.delete_recipe(id)
  elif option == 9:
    keyword = input('Enter Keyword To Search Recipe: ')
    Recipes.search_recipe(keyword)
  elif option == 10:
    print('Exit...')
    exit()
  else:
    print('Invalid option. Please try again.')

def main():
  while True:
    display_menu()
    try:
      choice = int(input('Enter your choice: '))
    except ValueError:
      print('Invalid Input. Please Enter a Number.')
      continue
    
    if choice == 10:
      handle_option(choice)
      break
    else:
      handle_option(choice)

if __name__ == "__main__":
    main()
