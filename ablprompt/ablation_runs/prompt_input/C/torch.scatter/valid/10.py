import torch

# Create input tensors
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
src_tensor = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
index_tensor = torch.tensor([[0, 1], [1, 0]], dtype=torch.long)

# Define the dimension along which to scatter
dim = 1

# Use torch.scatter to distribute values from src into input at positions specified by index
output_tensor = torch.scatter(input_tensor, dim, index_tensor, src_tensor)

print("Input Tensor:", input_tensor)
print("Source Tensor:", src_tensor)
print("Index Tensor:", index_tensor)
print("Output Tensor after scattering:", output_tensor)