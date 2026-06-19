import torch
from torch.utils.checkpoint import checkpoint_sequential

# Define a simple function to be used in checkpointing
def my_function(x):
    return x * x + 2 * x + 1

# Prepare valid input data
input_data = torch.randn(5)

# Call the API with the prepared input data
result = checkpoint_sequential([my_function], 1, input_data)
print(result)