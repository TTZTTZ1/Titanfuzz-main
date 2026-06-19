import torch

# Create a sample input tensor
input_tensor = torch.randn(4, 4)

# Create an index tensor
index_tensor = torch.tensor([[0, 1], [2, 3]])

# Create a source tensor
source_tensor = torch.tensor([[99, 88], [77, 66]])

# Use torch.scatter to distribute values from source_tensor into input_tensor
result_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nIndex Tensor:")
print(index_tensor)
print("\nSource Tensor:")
print(source_tensor)
print("\nResult Tensor:")
print(result_tensor)