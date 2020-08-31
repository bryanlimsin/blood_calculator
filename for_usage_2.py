foods = ["apples", "bananas", "cherries", "donuts"]


amounts = [11, 22, 33, 44]



def my_func(x, y):

    # Take input of food
    # Return amount

    food_taken = input("apples, bananas, cherries or donuts. Choose 1 only: ")
    for i, u in zip(x, y):
        if i == food_taken:
            print("There are {} left".format(u))
    
        else:
            print("input not valid")
            break # Need break so that it does not print the above multiple times


if __name__ == "__main__":
    my_func(foods, amounts)
