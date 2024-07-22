# mealplanner.py
# A text based program designed to help users organise their cooking
# Allows users to store recipes and create mealplans using those recipes
# Can display mealplans along with corresponding ingredients and recipes
# Author: Sydney Liu
# 27/06/2024

def store_recipes_submenu(recipes_list):
    repeat = True
    while repeat:
        option_store_recipes = input("Enter an option:")
        print("\n1.Add dish\n2.Remove dish\n3.Modify ingredients\n4.Modify steps\n5.Modify category\n6.Modify name\n7.Quit")
        if option_store_recipes == "1":
            input_name = input("Enter the dish name:")
            input_ingredients = input("Enter or paste the ingredients:")
            input_recipe = input("Enter or paste the recipe:")
            input_category = input("Enter category (1 for breakfast, 2 for lunch, 3 for dinner, seperated by commas):")
            add_dish(input_name, input_ingredients, input_recipe, input_category, recipes_list)           

        elif option_store_recipes == "2":
            input_name = input("Enter the dish name:")
            remove_dish()

        elif option_store_recipes == "3":
        elif option_store_recipes == "4":
            
        elif option_store_recipes == "5":
            
        elif option_store_recipes == "6":
            
        elif option_store_recipes == "7":
            repeat = False
        else:
            print("I don't understand.")


def add_dish(name, ingredients, recipe, category, list_of_recipes):
    list_of_recipes.append({"name": name, "ingredients": ingredients, "recipe": recipe, "category": category})


def remove_dish(name, list_of_recipes):
    for dish in list_of_recipes:
        if dish["name"] == name:
            list_of_recipes.remove(dish)


def planning_sub_menu(recipes_list):
    repeat = True
    while repeat:
        option_store_recipes = input("Enter an option:")
        print()

def menu(list_of_recipes):
    while True:
        print("Welcome to my program, designed to help you organise your cooking.\n")
        option = input("Enter an option:")
        print("\n1.Store your recipes\n2.Plan your meals\n3.Quit")
        if option == "1":
            store_recipes_submenu(list_of_recipes)

        elif option == "2":
            planning_sub_menu(list_of_recipes)
        
        elif option == "3":
            break

        else:
            print("I don't understand.")

if __name__ == "__main__":
    recipes = []
            
    
    
