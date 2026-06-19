import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.tensor([-4.0, -1.0, 0.0, 1.0, 4.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
result = torch.sqrt(input_tensor)

print(result)