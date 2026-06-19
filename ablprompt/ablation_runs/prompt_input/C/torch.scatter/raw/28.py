import torch

# Create a sample input tensor
input_tensor = torch.randn(3, 4)

# Create an index tensor
index_tensor = torch.tensor([[0, 1, 2, 0], [2, 0, 1, 2], [1, 2, 0, 1]])

# Create a source tensor
source_tensor = torch.randn(3, 4)

# Perform the scatter operation
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)