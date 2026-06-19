import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Insert a new dimension at index 0
output_tensor = torch.unsqueeze(input_tensor, 0)

print(output_tensor.shape)  # Output should be (1, 3, 4)