import torch

# Create a random input tensor
input_tensor = torch.randn(4, 5)

# Create a random index tensor
index_tensor = torch.randint(0, 5, (4,))

# Create a source tensor with the same shape as the index tensor
source_tensor = torch.rand(4,)

# Perform the scatter operation
output_tensor = torch.scatter(input_tensor, 1, index_tensor.unsqueeze(1), source_tensor)

print("Input Tensor:", input_tensor)
print("Index Tensor:", index_tensor)
print("Source Tensor:", source_tensor)
print("Output Tensor:", output_tensor)