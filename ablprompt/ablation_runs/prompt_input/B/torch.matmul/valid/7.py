import torch

# Create two random tensors with compatible shapes for batched matrix multiplication
batch_size = 3
input_tensor = torch.randn(batch_size, 4, 5)
other_tensor = torch.randn(batch_size, 5, 6)

# Perform batched matrix multiplication
result = torch.matmul(input_tensor, other_tensor)

print(result)