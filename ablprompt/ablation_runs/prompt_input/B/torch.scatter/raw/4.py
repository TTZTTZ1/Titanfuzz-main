import torch

# Create some tensors
input_tensor = torch.randn(4, 5)
index_tensor = torch.randint(0, 4, (4, 5))
source_tensor = torch.randn(4, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor
output_tensor = torch.scatter(input_tensor, 0, index_tensor, source_tensor)

print(output_tensor)