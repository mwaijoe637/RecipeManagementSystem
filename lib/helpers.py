import mysql.connector

mydb = mysql.connector.connect(
  user="root",
  database="recipe_manager"
)

mycursor = mydb.cursor()

class Ingredients():
  def create_ingredient(name):
    if not(name.strip()):
      print('Name Cant Be Blank')
    sql = "INSERT INTO ingredient (name) VALUES (%s)"
    val = (name,)
    mycursor.execute(sql, val)

    mydb.commit()
    print(f"Ingredient '{name}' Added Successfully!")


  def read_ingredients():
    mycursor.execute("SELECT * FROM ingredient")
    ingredients = mycursor.fetchall()

    for ingredient in ingredients:
      print(f'{ingredient[0]}) {ingredient[1]}\n')

  def update_ingredient(id, name):
    if not(name.strip()):
      print('Name Cant Be Blank')
    sql = "UPDATE ingredient SET name = %s WHERE ingredient_id = %s"
    val = (name, id)
    mycursor.execute(sql, val)

    mydb.commit()
    print(f"Ingredient '{name}' Updated Successfully!")

  def delete_ingredient(id):
    sql = "DELETE FROM ingredient WHERE ingredient_id = %s"
    val = (id,)
    mycursor.execute(sql, val)

    mydb.commit()
    print(f"Ingredient Deleted Successfully!")

class Recipes():
  def create_recipe(name, description, cuisine, dietary):
    if not(name.strip()) or not(description.strip()) or not(cuisine.strip()) or not(dietary.strip()):
      print('All Feilds Must Not Be Blank')
    sql = "INSERT INTO recipe (name, description, cuisine, dietary) VALUES (%s, %s, %s, %s)"
    val = (name, description, cuisine, dietary)
    mycursor.execute(sql, val)

    mydb.commit()
    print(f"Recipe '{name}' Added Successfully!")

  def read_recipes():
    mycursor.execute("SELECT * FROM recipe")
    recipes = mycursor.fetchall()

    for recipe in recipes:
      print(f'{recipe[0]}) {recipe[1]}\n')

  def read_recipe_info(id):
    sql = "SELECT * FROM recipe WHERE recipe_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    recipe = mycursor.fetchone()

    print(f'Name: {recipe[1]})\nDescription: {recipe[2]}\nCuisine: {recipe[3]}\nDietary: {recipe[4]}\n')

    sql = "SELECT ingredient_id FROM recipe_ingredient WHERE recipe_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    ingredient_ids = mycursor.fetchall()
    if ingredient_ids == None:
      print('No ingredients added to this recipe\n')
    else:
      ingredients = []
      for ingredient_id in ingredient_ids:
        sql = "SELECT * FROM ingredient WHERE ingredient_id = %s"
        val = (ingredient_id[0],)
        mycursor.execute(sql, val)
        ingredient = mycursor.fetchone()[1]
        ingredients.append(ingredient)
      print('Ingredients:\n')
      for ingredient in ingredients:
        print(ingredient)

  def update_recipe(id, name, description, cuisine, dietary):
    sql = "SELECT * FROM recipe WHERE recipe_id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    recipe = mycursor.fetchone()
    name = recipe[1] if not(name.strip()) else name
    description = recipe[2] if not(description.strip()) else description
    cuisine = recipe[3] if not(cuisine.strip()) else cuisine
    dietary = recipe[4] if not(dietary.strip()) else dietary

    sql = "UPDATE recipe SET name = %s, description = %s, cuisine = %s, dietary = %s WHERE recipe_id = %s"
    val = (name, description, cuisine, dietary, id)
    mycursor.execute(sql, val)

    mydb.commit()
    print(f"Recipe '{name}' Updated Successfully!")
    

  def delete_recipe(id):
    sql = "DELETE FROM recipe WHERE recipe_id = %s"
    val = (id,)
    mycursor.execute(sql, val)

    mydb.commit()

  def search_recipe(keyword):
    sql = "SELECT recipe_id, name FROM recipe WHERE LOWER(CONCAT(name, '', description, '', cuisine, '', dietary)) LIKE LOWER(CONCAT('%', %s, '%'))"
    val = (keyword,)
    mycursor.execute(sql, val)

    recipes = mycursor.fetchall()

    for recipe in recipes:
      print(f'{recipe[0]}) {recipe[1]}\n')


class RecipeIngredients():
  def create(ingredient_id, recipe_id):
    sql = "INSERT INTO recipe_ingredient (ingredient_id, recipe_id) VALUES (%s, %s)"
    val = (ingredient_id, recipe_id)
    mycursor.execute(sql, val)

    mydb.commit()

  def delete(ingredient_id, recipe_id):
    sql = "DELETE FROM recipe_ingredient WHERE ingredient_id = %s AND recipe_id = %s"
    val = (ingredient_id, recipe_id)
    mycursor.execute(sql, val)

    mydb.commit()
    print(f"Recipe Deleted Successfully!")