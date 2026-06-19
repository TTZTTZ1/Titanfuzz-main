import torch

# Create example tensors
input_tensor = torch.tensor([[1, 2], [3, 4]])
index_tensor = torch.tensor([[0, 1], [1, 0]])
source_tensor = torch.tensor([[5, 6], [7, 8]])

# Perform scatter operation
result_tensor = torch.scatter(input_tensor.clone(), 1, index_tensor, source_tensor)

print("Original Input Tensor:")
print(input_tensor)
print("Index Tensor:")
print(index_tensor)
print("Source Tensor:")
print(source_tensor)
print("Resulting Tensor after Scatter Operation:")
print(result_tensor)