import torch

# Create a 3x3 tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a 3x3 tensor of indices
index_tensor = torch.tensor([[0, 2, 1], [2, 0, 1], [1, 2, 0]])

# Use torch.gather to gather elements
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, 1))

print(output_tensor)