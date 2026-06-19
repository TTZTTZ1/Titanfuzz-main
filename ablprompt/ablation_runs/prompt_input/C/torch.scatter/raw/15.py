import torch

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Create an index tensor with the same shape as input_tensor but filled with indices
index_tensor = torch.randint(0, 4, (3, 4))

# Create a source tensor with the same shape as index_tensor
source_tensor = torch.rand(3, 4)

# Use torch.scatter to distribute values from source_tensor into input_tensor at positions specified by index_tensor along dimension 1
output_tensor = torch.scatter(input_tensor.clone(), 1, index_tensor, source_tensor)

print("Input Tensor:\n", input_tensor)
print("Index Tensor:\n", index_tensor)
print("Source Tensor:\n", source_tensor)
print("Output Tensor after scatter operation:\n", output_tensor)