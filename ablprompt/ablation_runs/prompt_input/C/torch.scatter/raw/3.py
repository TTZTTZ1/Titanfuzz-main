import torch

# Create example tensors
input_tensor = torch.tensor([[1, 2], [3, 4]])
index_tensor = torch.tensor([[0, 1], [1, 0]])
source_tensor = torch.tensor([[5, 6], [7, 8]])

# Use torch.scatter
result_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(result_tensor)