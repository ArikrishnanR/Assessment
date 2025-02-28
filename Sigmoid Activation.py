import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#test cases
if __name__ == "__main__":
    #single values
    print("Sigmoid(-2):", sigmoid(-2))  
    print("Sigmoid(0):", sigmoid(0))
    print("Sigmoid(2):", sigmoid(2))    
    
    #array values
    arr = np.array([-2, -1, 0, 1, 2])
    print("Sigmoid applied to array:", sigmoid(arr))
    
    
    
'''
explain:
At 0% turn (x = -∞) → Light is OFF (Sigmoid ≈ 0)
50% turn (x = 0) → Light is half-bright (Sigmoid = 0.5)
At 100% turn (x = ∞) → Light is turned ON completely (Sigmoid ≈ 1)
'''