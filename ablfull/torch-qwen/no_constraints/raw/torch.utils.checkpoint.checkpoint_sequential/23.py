import torch
from torch.utils.checkpoint import checkpoint_sequential

# Define a simple sequential function
def simple_function(x):
    return x * x + 2 * x + 1

# Prepare input data
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Call the API
result = checkpoint_sequential((simple_function,), 1, input_data)

print(result)