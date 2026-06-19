import torch

# Define a simple function to be checkpointed
def my_function(x):
    return x * x + x + 1

# Create input data
input_data = torch.randn(10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential([my_function], 1, input_data)
print(output)