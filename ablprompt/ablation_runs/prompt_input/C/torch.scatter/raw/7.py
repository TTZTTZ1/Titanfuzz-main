import torch

# Create a random input tensor
input_tensor = torch.randn(4, 5)

# Create an index tensor
index_tensor = torch.randint(0, 5, (4,))

# Create a source tensor
source_tensor = torch.rand(4, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor
output_tensor = torch.scatter(input_tensor, 1, index_tensor.unsqueeze(1), source_tensor)

print("Input Tensor:\n", input_tensor)
print("Index Tensor:\n", index_tensor)
print("Source Tensor:\n", source_tensor)
print("Output Tensor:\n", output_tensor)