import numpy as np

def relu(x):
    return np.maximum(0, x)

#get user input
def get_user_input():
    user_input = input("Enter a numbers (example: -2 -1 0 1 2): ")
    input_list = [float(x) for x in user_input.split()]
    return np.array(input_list)

# Main program
if __name__ == "__main__":
    #user input
    input_data = get_user_input()

    #apply ReLU
    output_data = relu(input_data)

    #print results
    print("Input Data:", input_data)
    print("Output Data (after ReLU):", output_data)
    
    
'''
explain
User Input:
The get_user_input() function asks the user to input a list of numbers separated by spaces.
The input is separated into individual strings, are converted to floats, and are stored in a NumPy array.

ReLU Calculation:
The relu() function calculates the ReLU activation for the input given by the user.

Output:
The program prints the original input and the output after the ReLU function has been applied.
'''