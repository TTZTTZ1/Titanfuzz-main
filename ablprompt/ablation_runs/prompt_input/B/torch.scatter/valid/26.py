import torch

# Create some example tensors
input_tensor = torch.randn(3, 4)
index_tensor = torch.tensor([[0, 1], [2, 0]])
source_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Perform the scatter operation
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)