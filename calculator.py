# hi testing if pyhon syntax works here on Jupyter.


def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return

        elif choice == "1":
            HDL_driver()
            return
        
        elif choice == "2":
            LDL_driver()
            return
            

def HDL_driver():

    # Get the input
    input_to_check = input_function()

    # Check if HDL is normal
    final_output = check_HDL(input_to_check)

    # Have an output
    out_analysis(input_to_check, final_output)



def LDL_driver():

    # Get the input
    input_to_check = input_function_2()
    
    # Check if HDL is normal
    final_output = check_LDL(input_to_check)

    # Have an output
    out_analysis_2(input_to_check, final_output)



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


####################################################################################
# Modular functions to be used in LDL_driver()

def input_function_2():
    x = input("Enter your LDL value: ")
    x = int(x)
    return x


# Check if LDL is normal

def check_LDL(y):
    LDL_value = y

    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    elif 160 <= LDL_value <= 189:
        return "High"
    elif LDL_value >= 190:
        return "Very high"

# Have an output
def out_analysis_2(x, y):
    print("The LDL result is {}".format(x))
    print("The analysis is {}".format(y))



interface() # notice running this function after defining all the modules above is correct 







