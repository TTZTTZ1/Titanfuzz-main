import torch

# Create random tensors with shapes that support batched matrix multiplication
batch_size = 2
input_tensor = torch.randn(batch_size, 3, 4)
other_tensor = torch.randn(batch_size, 4, 5)

# Perform batched matrix multiplication
result = torch.matmul(input_tensor, other_tensor)

print(result)