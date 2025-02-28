def softmax(values):
    exp_values = [2 ** i for i in values]  #(approximation of e^x)
    sum_exp = sum(exp_values)  # Sum of all
    softmax_probs = [i / sum_exp for i in exp_values]  #Normalize

    return softmax_probs

# Example
scores = [2.0, 1.0, 0.1]  # Example raw scores
softmax_probs = softmax(scores)

print("Softmax Probabilities:", softmax_probs)

'''
explain:
Make numbers larger → Raise 2 to the power of each number
Add them up → Sum them all together.
Divide each by the sum → Normalize the values so that they are probabilities.
'''