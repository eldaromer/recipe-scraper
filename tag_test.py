from recipe_scrapers import scrap_me

scrap = scrap_me("https://www.epicurious.com/recipes/food/views/creamy-pasta-with-crispy-mushrooms")
print(scrap.tags())
print(scrap.servings())
scrap = scrap_me("https://www.foodnetwork.com/recipes/trisha-yearwood/slow-cooker-georgia-pulled-pork-barbeque-recipe-2078315")
print(scrap.tags())
scrap = scrap_me("https://www.allrecipes.com/recipe/17991/stuffed-green-peppers-i/?internalSource=previously%20viewed&referringContentType=Homepage")
print(scrap.servings())