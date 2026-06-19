import torch

# Define a simple function to act as a layer
def simple_layer(x):
    return x * 2

# Create a sequential model or list of layers
functions = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.ReLU(), torch.nn.Linear(5, 1))
# Alternatively, as a list of functions
# functions = [lambda x: x * 2, lambda x: x + 3]

# Prepare input data
input_data = torch.randn(1, 10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments=2, input=input_data, use_reentrant=True)
print(result)