"""
Calculates recipe ingredient amounts based on the quantity of an
item. Each item is unique to each recipe.

Each function with a _scale suffix calculates the ingredients based
on an ingredient multiplier. 

"""

def tinga(chick_lbs):

    """
    float --> list
    Avg # romas in 28oz can is 11. Ro
    """

    scale = chick_lbs / (1.25)
    oil = 2 * scale
    tom_til = 2 * scale
    gar = 4 * scale
    oni = 1 * scale
    oreg = 2 * scale
    bay = 2 * scale
    cid = 2 * scale
    stk = 2 * scale
    chp = 2.5 * scale
    chp_sau = 1 * scale
    fsh = 2 * scale

    print("Scale is " + str(scale) + " for " + str(lbs) + " lbs of chicken", end = '\n\n')
    print("Ing List:", end = '\n\n')
    print(str(oil) + " Tablespoon of vegetable oil")
    print(str(tom_til) + " Tomatillos and tomatoes")
    print(str(gar) + " Cloves of garlic")
    print(str(oni) + " White onions, finely chopped")
    print(str(oreg) + " Teasponns of oregano")
    print(str(bay) + " Bay leaves")
    print(str(cid) + " Tablespoons of cider vinegar")
    print(str(stk) + " Cups of chicken stock")
    print(str(chp) + " Chipotles in adodo sauce and ")
    print(str(chp_sau) + " Tablespoons of adobo sauce")
    print(str(fsh) + " Teaspoons of fish sauce")

def tinga_scale(scale):
    tinga(scale*1.25)

def granola(oat_g):
    if isinstance(oat_g, str):
        return print("Recipe: https://www.seriouseats.com/recipes/2017/06/crispy-homemade-granola-recipe.html\nEnter a number for oats in grams. The function returns an ingredient list. All numbers are rounded down except salt and table- and teaspoons, which are rounded to two decimals.\n1 stick of butter = 115g")
    scale = oat_g / 12
    germ = scale * 40
    flax = scale * 30
    chia = scale * 15
    milk = scale * 8
    butter = scale * 115
    sugar = scale * 200
    salt = scale * 2
    #Mix-Ins
    pump = scale * 120
    alm = scale * 70
    pec = scale * 65
    oil = scale
    salt2 = scale * .75
    apr = scale * 115
    cher = scale * 85
    blue = scale * 55

    print("Scale is " + str(round(scale, 2)) + " for " + str(int(oat_g)) + " grams of oats", end = '\n\n')
    print("Granola Ingredients:", end = '\n\n') # Granola
    print(str(int(oat_g)) + " Grams of oats")
    print(str(int(germ)) + " Grams of wheat germ ")
    print(str(int(flax)) + " Grams of flax seeds")
    print(str(int(chia)) + " Grams of chia seeds")
    print(str(int(milk)) + " Ounces of buttermilk")
    print(str(int(butter)) + " Grams of butter")
    print(str(int(sugar)) + " Grams of sugar")
    print(str(round(salt, 1)) + " Grams of salt")
    print("Med bowl: Oats, germ, flax, chia, then add butter and milk, 20 min")
    print("Prep bowl: Sugar, salt, 30 min")
    print("bake @ 300, 100 min, 4 stirs", end = '\n\n\n')

    
    print("Mix-in Ingredients:", end = '\n\n') # Mix-Ins
    print(str(int(pump)) + " Grams pumpkin seeds ")
    print(str(int(alm)) + " Grams of almond slivers")
    print(str(int(pec)) + " Grams of pecan pieces")
    print(str(round(oil, 1)) + " Teaspoons of neutral vegetable oil")
    print(str(round(salt2, 1)) + " Grams of salt")
    print(str(int(apr)) + " Grams of apricots")
    print(str(int(cher)) + " Grams of sour cherries")
    print(str(int(blue)) + " Grams of blueberries")
    print("Small bowl: Pumpkin, Almonds, Pecan. Bake 10 min @ 350")
    print("Large bowl: ^ then Salt, Oil, then fruits", end = '\n\n')

    
def granola_scale(scale):
    granola(scale*12)
    
