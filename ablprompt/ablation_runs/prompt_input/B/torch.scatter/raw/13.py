import torch

# Create input tensors
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
src_tensor = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
index_tensor = torch.tensor([[0, 1], [1, 0]], dtype=torch.int64)

# Define the dimension along which to scatter
dim = 1

# Use torch.scatter to distribute values from src_tensor into input_tensor
output_tensor = torch.scatter(input_tensor, dim, index_tensor, src_tensor)

print(output_tensor)