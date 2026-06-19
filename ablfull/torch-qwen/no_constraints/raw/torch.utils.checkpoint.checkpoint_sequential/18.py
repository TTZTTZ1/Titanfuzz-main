import torch

# Define a simple sequential function
def simple_function(x):
    return x * x + 2 * x + 1

# Create a list of functions to be checkpointed
functions = [simple_function] * 3

# Prepare input data
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)

print(output)