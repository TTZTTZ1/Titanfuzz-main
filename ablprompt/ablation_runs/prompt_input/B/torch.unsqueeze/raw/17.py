import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Insert a new dimension at index 1
output_tensor = torch.unsqueeze(input_tensor, 1)

print(output_tensor.shape)