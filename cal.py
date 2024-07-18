import sympy as sp

# Define the variables
W, P = sp.symbols('W P')

# Define the expression
expression = (1 / (6 * P)) * (W * (W**2 + 3*W + 2) / (W + 1)**2)

# Simplify the expression (optional)
simplified_expression = sp.simplify(expression)

# Function to calculate the value of the expression for given W and P
def calculate_expression(w_value, p_value):
    return simplified_expression.evalf(subs={W: w_value, P: p_value})

# Input values for W and P
w_value = 40
p_value = 60

# Calculate and print the result
result = calculate_expression(w_value, p_value)
print(f"The result of the expression for W={w_value} and P={p_value} is: {result}")
