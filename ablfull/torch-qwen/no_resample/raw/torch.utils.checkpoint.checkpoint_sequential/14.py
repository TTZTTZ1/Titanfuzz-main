import torch
from torch.nn import Sequential, Linear

# Define the function to be checkpointed
def my_function(x):
    return x * 2

# Create a sequential model
model = Sequential(Linear(10, 5), Linear(5, 1))

# Prepare input data
input_data = torch.randn(1, 10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential([my_function], 1, input_data, use_reentrant=True)