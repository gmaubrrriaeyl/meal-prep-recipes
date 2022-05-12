"""
Calculates recipe ingredient amounts based on the quantity of an
item. Each item is unique to each recipe.

Each function with a _scale suffix calculates the ingredients based
on an ingredient multiplier. 

"""

tinga = [
    {"name": "chick", "scale": 1.25, "text" : "lbs of chicken"},
    
    {"name": "oil", "scale": 2, "text": "Tablespoon of vegetable oil"},
    {"name": "tom_til", "scale": 2, "text": "Tomatillos and tomatoes"},
    {"name": "gar", "scale": 4, "text": "Cloves of garlic"},
    {"name": "oni", "scale": 1, "text": "White onions, finely chopped"},
    {"name": "oreg", "scale": 2, "text": "Teasponns of oregano"},
    {"name": "bay", "scale": 2, "text": "Bay leaves"},
    {"name": "cid", "scale": 2, "text": "Tablespoons of cider vinegar"},
    {"name": "stk", "scale": 2, "text": "Cups of chicken stock"},
    {"name": "chp", "scale": 2, "text": "Chipotles in adodo sauce and "},
    {"name": "chp_sau", "scale": 1, "text": "Tablespoons of adobo sauce"},
    {"name": "fsh", "scale": 2, "text": "Teaspoons of fish sauce"},
]

granola = [
    {"name": "oat", "scale": 340, "text": "Grams of oats"},
    {"name": "germ", "scale": 40, "text": "Grams of wheat germs"},
    {"name": "flax", "scale": 30, "text": "Grams of flax seeds"},
    {"name": "chia", "scale": 15, "text": "Grams of chia seeds"},
    {"name": "milk", "scale": 8, "text": "Ounces of buttermilk"},
    {"name": "butter", "scale": 115, "text": "Grams of butter"},
    {"name": "sugar", "scale": 200, "text": "Grams of sugar"},
    {"name": "salt", "scale": .5, "text": "Grams of salt"},
    {"name": "pump", "scale": 120, "text": "Grams of pumpkin seeds"},
    {"name": "alm", "scale": 70, "text": "Grams of sliced almonds"},
    {"name": "pec", "scale": 65, "text": "Grams of pecan pieces"},
    {"name": "oil", "scale": 1, "text": "Teaspoons of neutral oil"},
    {"name": "salt2", "scale": 1/8, "text": "Teaspoons of salt"},
    {"name": "apr", "scale": 115, "text": "Grams of apricot"},
    {"name": "cher", "scale": 85, "text": "Grams of cherries"},
    {"name": "blue", "scale": 55, "text": "Grams of blueberries"},
]
cit_stk = [
    {"name": "citrus", "scale": 1000, "text": "Grams of citrus rines"},
    {"name": "water", "scale": 1500, "text": "Mililiters of water"},
    {"name": "sugar", "scale": 70, "text": "Grams of sugar"},
    {"name": "malic", "scale": 10, "text": "Grams of malic"},
    {"name": "citric", "scale": 20, "text": "Grams of citic"},
]

nutella = [
    {"name": "hazelnuts", "scale": 255, "text": "Grams of hazelnuts"},
    {"name": "water", "scale": 85, "text": "Grams/Ml of water"},
    {"name": "sugar", "scale": 150, "text": "Grams of sugar"},
    {"name": "syrup", "scale": 115, "text": "Grams of golden/corn syrup"},
    {"name": "salt", "scale": 2.5, "text": "Grams of salt"},
    {"name": "baking soda", "scale": 3, "text": "Grams of baking soda"},
    {"name": "cocoa", "scale": 15, "text": "Grams of cocoa powder"},
    {"name": "hazel_oil", "scale": 30, "text": "Grams of hazelnut oil"},
]
def ing_calc(ing_list, ing, am):
    for i in ing_list:
        if i['name']==str(ing):
            text = i['text']
            scale = round(am / i['scale'], 2)
    print(f"Scale is {scale} for {am} {text}")
    print("Ing List:\n")

    for ing in ing_list:
        print(f'{round(ing["scale"]*scale, 2)} {ing["text"]}')
