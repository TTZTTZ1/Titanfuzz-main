import torch

# Define a simple function to be checkpointed
def my_function(x):
    return x * x + 2 * x + 1

# Prepare input data
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential([my_function], 1, input_data)
print(result)