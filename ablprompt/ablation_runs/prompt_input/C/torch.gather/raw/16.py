import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Create an index tensor
index_tensor = torch.tensor([[0, 0], [1, 0]])

# Use torch.gather to select elements
output_tensor = torch.gather(input_tensor, 1, index_tensor)

print(output_tensor)