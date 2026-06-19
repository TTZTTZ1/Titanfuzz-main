import torch

# Create input tensors
input_tensor = torch.randn(4, 5)
src_tensor = torch.randn(4, 5)
index_tensor = torch.randint(0, 5, (4, 5))

# Use torch.scatter to distribute values from src_tensor into input_tensor at positions specified by index_tensor along dimension 1
output_tensor = torch.scatter(input_tensor.clone(), 1, index_tensor, src_tensor)

print(output_tensor)