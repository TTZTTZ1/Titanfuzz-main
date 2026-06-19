import torch

# Create some example tensors
input_tensor = torch.randn(4, 5)
src_tensor = torch.randn(4, 5)
index_tensor = torch.randint(0, 5, (4, 5))

# Use torch.scatter
output_tensor = torch.scatter(input_tensor, 1, index_tensor, src_tensor)

print(output_tensor)