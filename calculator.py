# hi testing if pyhon syntax works here on Jupyter.


def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return

        elif choice == "1":
            HDL_driver()
            return
            

def HDL_driver():

    # Get the input
    
    input_to_check = input_function()


    # Check if HDL is normal
    
    final_output = check_HDL(input_to_check)

    # Have an output

    out_analysis(input_to_check, final_output)



####################################################################################
# Modular functions to be used in HDL_driver()

def input_function():
    x = input("Enter your HDL value: ")
    x = int(x)
    return x


# Check if HDL is normal

def check_HDL(y):
    HDL_value = y

    if HDL_value > 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

# Have an output

def out_analysis(x, y):
    print("The HDL result is {}".format(x))
    print("The analysis is {}".format(y))


interface() # notice running this function after defining all the modules above is correct 







