import torch

# Create a sample input tensor
input_tensor = torch.randn(4, 5)

# Create a sample index tensor
index_tensor = torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]])

# Create a sample source tensor
source_tensor = torch.randn(2, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor
result_tensor = torch.scatter(input_tensor, 0, index_tensor, source_tensor)

print(result_tensor)