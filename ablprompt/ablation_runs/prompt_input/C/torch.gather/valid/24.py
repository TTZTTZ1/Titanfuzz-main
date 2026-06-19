import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create an index tensor
index_tensor = torch.tensor([[0, 2, 1], [2, 0, 1]])

# Use torch.gather to gather elements from input_tensor based on index_tensor along dim=1
gathered_tensor = torch.gather(input_tensor, 1, index_tensor)

print(gathered_tensor)
# Output should be: tensor([[1, 3, 2], [6, 4, 5]])