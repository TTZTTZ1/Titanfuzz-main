import torch

# Create a sample input tensor
input_tensor = torch.randn(3, 4)

# Create an index tensor
index_tensor = torch.LongTensor([[0, 1, 2, 3], [2, 3, 0, 1], [1, 0, 3, 2]])

# Use torch.gather to select elements
output_tensor = torch.gather(input_tensor, 1, index_tensor)

print("Input Tensor:")
print(input_tensor)
print("Index Tensor:")
print(index_tensor)
print("Output Tensor:")
print(output_tensor)