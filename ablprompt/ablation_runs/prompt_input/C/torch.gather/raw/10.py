import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Define the dimension along which to gather
dim = 1

# Create an index tensor specifying the positions to gather
index_tensor = torch.tensor([[0, 2, 1], [2, 1, 0]])

# Use torch.gather to gather elements from input_tensor based on index_tensor
output_tensor = torch.gather(input_tensor, dim, index_tensor)

print("Input Tensor:")
print(input_tensor)
print("Index Tensor:")
print(index_tensor)
print("Output Tensor:")
print(output_tensor)