import torch

# Create a sample input tensor
input_tensor = torch.randn(4, 4)

# Create a sample index tensor
index_tensor = torch.tensor([[0, 1], [2, 3]])

# Create a sample source tensor
source_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Use torch.scatter to distribute values from source_tensor into input_tensor
result_tensor = torch.scatter(input_tensor.clone(), 0, index_tensor.unsqueeze(-1).expand_as(source_tensor), source_tensor)

print(result_tensor)