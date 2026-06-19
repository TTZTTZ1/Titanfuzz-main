import torch

# Create example tensors
input_tensor = torch.randn(4, 5)
index_tensor = torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]])
source_tensor = torch.arange(10).view(2, 5)

# Perform scatter operation
result_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(result_tensor)