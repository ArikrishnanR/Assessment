def MSE(y_true, y_pred):
    n = len(y_true)  
    mse = 0
    for i in range(n):
        error = y_true[i] - y_pred[i]  #Difference to actual and predicted
        mse += error ** 2  #Squaring the error
    return mse / n  #Average of mse 

# Example
actual = [3, -0.5, 2, 7]   #Actual values
predicted = [2.5, 0.0, 2, 8]  #Predicted values

mse_value = MSE(actual, predicted)
print("Mean Squared Error(MSE):", mse_value)


"""

explain:

accepts two lists (y_true and y_pred) as arguments.
Iterates over all the values, computes the error (y_true - y_pred).
Squares the mistake and adds them up.
Divides by the total number of values to get the final MSE

"""
