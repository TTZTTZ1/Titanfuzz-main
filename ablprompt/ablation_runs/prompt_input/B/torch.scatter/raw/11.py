import torch

# Create a random input tensor
input_tensor = torch.randn(5, 5)

# Create an index tensor with the same shape as the input tensor
index_tensor = torch.randint(0, 5, (5, 5))

# Create a source tensor with the same shape as the index tensor
source_tensor = torch.randn(5, 5)

# Perform the scatter operation along dimension 0
result_tensor = torch.scatter(input_tensor, 0, index_tensor, source_tensor)

print(result_tensor)