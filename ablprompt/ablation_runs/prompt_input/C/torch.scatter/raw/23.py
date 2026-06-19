import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Create an index tensor specifying where to scatter the values
index_tensor = torch.tensor([[0, 1], [1, 0]])

# Create a source tensor containing the values to be scattered
source_tensor = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Use torch.scatter to distribute values from source_tensor into input_tensor
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)