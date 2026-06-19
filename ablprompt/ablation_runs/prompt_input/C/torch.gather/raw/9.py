import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create an index tensor specifying the positions to gather
index_tensor = torch.tensor([[0, 2, 1], [2, 0, 1]])

# Use torch.gather to select elements from the input tensor based on the index tensor
output_tensor = torch.gather(input_tensor, 1, index_tensor)

print(output_tensor)
# Expected Output: tensor([[1, 3, 2], [6, 4, 5]])