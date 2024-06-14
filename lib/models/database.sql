CREATE DATABASE recipe_manager;

USE recipe_manager;

CREATE TABLE ingredient(
  ingredient_id int AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(15) NOT NULL
);

CREATE TABLE recipe(
  recipe_id int AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  description VARCHAR(150) NOT NULL,
  cuisine VARCHAR(800) NOT NULL,
  dietary VARCHAR(300) NOT NULL
);

CREATE TABLE recipe_ingredient(
  recipe_id int NOT NULL,
  ingredient_id int NOT NULL,
  FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id) ON DELETE CASCADE
);