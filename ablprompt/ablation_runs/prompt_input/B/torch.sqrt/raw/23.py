import torch

# Create a random tensor with negative values
input_tensor = torch.tensor([-1.0, 4.0, -9.0, 16.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
result = torch.sqrt(input_tensor)

print(result)