import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2], [3, 4], [5, 6]])

# Create an index tensor
index_tensor = torch.tensor([[0, 1], [1, 0], [1, 1]])

# Use torch.gather to select elements
gathered_tensor = torch.gather(input_tensor, 1, index_tensor)

print(gathered_tensor)