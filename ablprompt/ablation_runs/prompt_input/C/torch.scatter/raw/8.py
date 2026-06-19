import torch

# Create a random input tensor
input_tensor = torch.randn(4, 5)

# Create an index tensor with the same shape as input_tensor but filled with indices
index_tensor = torch.randint(0, 5, (4, 5))

# Create a source tensor with the same shape as index_tensor
source_tensor = torch.randn(4, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor at positions specified by index_tensor along dimension 1
result_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(result_tensor)