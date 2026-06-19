import torch

# Create a sample input tensor
input_tensor = torch.randn(3, 4)

# Create a sample index tensor
index_tensor = torch.tensor([[0, 1, 2, 0], [1, 2, 0, 1], [2, 0, 1, 2]])

# Create a sample source tensor
source_tensor = torch.ones_like(index_tensor)

# Perform the scatter operation
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)