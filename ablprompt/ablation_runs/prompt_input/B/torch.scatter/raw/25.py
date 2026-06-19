import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Define the indices where values will be scattered
indices = torch.tensor([[0, 1], [1, 0]])

# Create the source tensor with values to scatter
source_tensor = torch.tensor([[9, 8], [7, 6]])

# Perform the scatter operation
result = torch.scatter(input_tensor, 0, indices, source_tensor)

print(result)