import torch

# Create random tensors with compatible shapes for batched matrix multiplication
batch_size = 3
input_tensor = torch.randn(batch_size, 2, 3)
other_tensor = torch.randn(batch_size, 3, 4)

# Perform batched matrix multiplication
result = torch.matmul(input_tensor, other_tensor)

print(result)