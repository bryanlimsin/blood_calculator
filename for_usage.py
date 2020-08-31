foods = ["apples", "bananas", "cherries", "donuts"]


amounts = [11, 22, 33, 44]

for i, x in enumerate(foods):
    print("{} - {}".format(amounts[i], x))


#########
# With zip()


do_I_like_it = [True, False, False, True]

for y, x, z in zip(amounts, foods, do_I_like_it):
    print("{} - {} - {}".format(y,x,z))
