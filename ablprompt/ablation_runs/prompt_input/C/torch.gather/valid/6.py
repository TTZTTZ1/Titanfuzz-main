import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Define the dimension along which to gather
dim = 1

# Create an index tensor specifying the positions to gather from
index_tensor = torch.tensor([[0, 2, 1], [2, 0, 1]])

# Use torch.gather to select elements from the input tensor based on the index tensor
output_tensor = torch.gather(input_tensor, dim, index_tensor)

print("Input Tensor:", input_tensor)
print("Index Tensor:", index_tensor)
print("Output Tensor:", output_tensor)