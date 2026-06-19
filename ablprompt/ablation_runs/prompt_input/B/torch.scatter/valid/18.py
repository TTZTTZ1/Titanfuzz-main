import torch

# Create input tensors
input_tensor = torch.randn(4, 5)
src_tensor = torch.randn(4, 5)
index_tensor = torch.randint(0, 5, (4, 5))

# Define the dimension along which to scatter
dim = 1

# Use torch.scatter to distribute values from src into input at positions specified by index
output_tensor = torch.scatter(input_tensor, dim, index_tensor, src_tensor)

print(output_tensor)