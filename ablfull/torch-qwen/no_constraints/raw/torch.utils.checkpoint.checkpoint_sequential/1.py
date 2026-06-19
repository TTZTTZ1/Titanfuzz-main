import torch
from torch.nn import Linear

# Define some dummy functions
def func1(x):
    return x * 2

def func2(x):
    return x + 3

def func3(x):
    return x ** 2

functions = [Linear(10, 5), Linear(5, 10)]

# Generate input data
input_data = torch.randn(1, 10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, 2, input_data)