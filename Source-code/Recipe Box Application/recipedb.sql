/* TCSS600A - Independent study Project     
  Author: Sumitha Ravindran               
  Recipe Box Application */
  
create database recipeDB;
use recipeDB;

CREATE TABLE recipe_box (
    recipe_name VARCHAR(100) NOT NULL primary key,
    recipe_description VARCHAR(255) NOT NULL
    );
insert into recipe_box values('Coffee','Boil 100ml water with a spoon of coffee powder and add it to a cup of hot milk and serve');
insert into recipe_box values('Omelette',' 1.Take two eggs, pepper, salt, cheese'
                     ' 2.Blend everything using blender until you see some bubbles in the mix'
                     ' 3.Then pour your mix on a pan'
                     ' 4.Wait for a minute to cook');
insert into recipe_box values('Milk sweet','Boil 100ml water with half a litre of milk then add sugar to it, cook until the milk thickens');

select * from recipe_box;

