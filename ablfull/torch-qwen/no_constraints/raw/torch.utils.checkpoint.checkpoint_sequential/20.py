import torch

# Define a simple function to be checkpointed
def simple_function(x):
    return x * x + 2 * x + 1

# Create a sequential container of functions
functions = [simple_function] * 3

# Prepare input data
input_data = torch.tensor([1.0, 2.0, 3.0])

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)

print(output)