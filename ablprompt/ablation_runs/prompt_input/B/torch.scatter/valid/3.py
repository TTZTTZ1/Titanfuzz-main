import torch

# Create tensors
input_tensor = torch.tensor([[1, 2], [3, 4]])
index_tensor = torch.tensor([[0, 1], [1, 0]])
source_tensor = torch.tensor([[99, 88], [77, 66]])

# Use torch.scatter
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)