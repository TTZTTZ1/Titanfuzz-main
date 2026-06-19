import torch

# Create a random input tensor
input_tensor = torch.randn(4, 5)

# Create an index tensor with the same shape as the input tensor
index_tensor = torch.randint(0, 5, (4, 5))

# Create a source tensor with the same shape as the index tensor
source_tensor = torch.rand(4, 5)

# Use torch.scatter to distribute values from source_tensor into input_tensor
output_tensor = torch.scatter(input_tensor.clone(), 1, index_tensor, source_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nIndex Tensor:")
print(index_tensor)
print("\nSource Tensor:")
print(source_tensor)
print("\nOutput Tensor after scatter operation:")
print(output_tensor)