import torch

# Create input tensors
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
index_tensor = torch.tensor([[0, 1], [1, 0]])
source_tensor = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Perform scatter operation
output_tensor = torch.scatter(input_tensor.clone(), 1, index_tensor, source_tensor)

print(output_tensor)