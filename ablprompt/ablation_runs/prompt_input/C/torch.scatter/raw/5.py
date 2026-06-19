import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Define the indices where we want to scatter the values
indices = torch.tensor([[0, 1], [1, 0]])

# Create the source tensor with values to be scattered
source_tensor = torch.tensor([[9.0, 8.0], [7.0, 6.0]])

# Perform the scatter operation along dimension 1
output_tensor = torch.scatter(input_tensor, 1, indices, source_tensor)

print(output_tensor)