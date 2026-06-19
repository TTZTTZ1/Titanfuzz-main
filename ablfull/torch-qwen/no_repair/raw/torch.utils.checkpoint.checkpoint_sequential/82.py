import torch
from torch.nn import Sequential

# Define a simple function for testing
def test_function(x):
    return x * 2

# Create a sequential model with three layers
model = Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Prepare the input tensor
input_tensor = torch.randn(1, 10)

# Convert the model to a list of functions for checkpointing
functions = list(model.children())

# Set the number of segments
segments = 3

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=False)
print(result)