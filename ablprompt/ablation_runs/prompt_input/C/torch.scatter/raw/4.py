import torch

# Create some tensors
input_tensor = torch.randn(4, 5)
index_tensor = torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]])
source_tensor = torch.ones(2, 5)

# Perform scatter operation
output_tensor = torch.scatter(input_tensor, 0, index_tensor, source_tensor)

print(output_tensor)