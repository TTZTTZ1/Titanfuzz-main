import torch

# Create input tensors
input_tensor = torch.randn(4, 5)
index_tensor = torch.tensor([[0, 1], [2, 3]])
source_tensor = torch.tensor([[10, 20], [30, 40]])

# Use torch.scatter to distribute values
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)