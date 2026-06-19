import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create an index tensor specifying the gather positions
index_tensor = torch.tensor([[0, 2, 1], [2, 1, 0]])

# Use torch.gather to select elements based on the index tensor
gathered_tensor = torch.gather(input_tensor, 1, index_tensor)

print(gathered_tensor)