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
            

def HDL_driver():

    # Get the input
    
    def input_function():
        x = input("Enter your HDL value")
        return x


    # Check if HDL is normal
    
    def check_HDL():
        HDL_value = input_function()
        
        if HDL_value > 60:
            return "Normal"
        elif 40 <= HDL_value < 60:
            return "Borderline Low"
        else:
            return "Low"

    # Have an output



interface()







