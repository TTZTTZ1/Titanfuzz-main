import torch
from torch.utils.checkpoint import checkpoint_sequential

# Define a simple function to be used in checkpointing
def simple_function(x):
    return x * x + 2 * x + 1

# Prepare valid input data
input_data = torch.randn(5)

# Call the API
result = checkpoint_sequential([simple_function], 1, input_data)