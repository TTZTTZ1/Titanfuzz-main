import torch

# Create a random input tensor
input_tensor = torch.randn(4, 5)

# Create an index tensor with the same shape as the input tensor except for the first dimension
index_tensor = torch.randint(0, 4, (4, 5))

# Create a source tensor with the same shape as the index tensor
source_tensor = torch.randn(4, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor at positions specified by index_tensor along dimension 0
result_tensor = torch.scatter(input_tensor.clone(), 0, index_tensor, source_tensor)

print(result_tensor)