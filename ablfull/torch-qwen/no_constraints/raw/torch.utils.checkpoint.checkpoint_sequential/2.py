import torch

# Define a simple function to be checkpointed
def func(x):
    return x * x + 2 * x + 1

# Prepare input data
input_data = torch.randn(5)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential([func], 1, input_data)
print(result)