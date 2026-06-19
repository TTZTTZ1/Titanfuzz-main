import torch

# Create a 3x3 tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create an index tensor
index_tensor = torch.tensor([[0, 2, 1], [2, 0, 2], [1, 1, 0]])

# Use torch.gather to select elements
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, input_tensor.shape[2]))

print(output_tensor)