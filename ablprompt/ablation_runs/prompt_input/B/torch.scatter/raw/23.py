import torch

# Create a sample input tensor
input_tensor = torch.randn(4, 5)

# Create a sample index tensor
index_tensor = torch.randint(0, 5, (4,))

# Create a sample source tensor
source_tensor = torch.randn(4, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor at positions specified by index_tensor along dimension 1
result_tensor = torch.scatter(input_tensor, 1, index_tensor.unsqueeze(-1).expand_as(source_tensor), source_tensor)

print(result_tensor)