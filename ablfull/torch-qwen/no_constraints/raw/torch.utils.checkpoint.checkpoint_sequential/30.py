import torch

# Define a simple function to be checkpointed
def my_function(x):
    return x * x + 2 * x + 1

# Create a sequential container of functions
functions = [my_function]

# Prepare valid input data
input_data = torch.randn(5)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)