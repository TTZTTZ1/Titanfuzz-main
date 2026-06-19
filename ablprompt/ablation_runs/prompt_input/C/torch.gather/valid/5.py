import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Create an index tensor
index_tensor = torch.tensor([[0, 0], [1, 0]])

# Use torch.gather to gather elements from the input tensor based on the index tensor
gathered_tensor = torch.gather(input_tensor, 1, index_tensor)

print(gathered_tensor)
# Expected output: tensor([[1, 1], [4, 3]])