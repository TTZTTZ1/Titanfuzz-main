import torch

# Create a random tensor with negative and positive values
input_tensor = torch.tensor([-4.0, 9.0, 16.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
result_tensor = torch.sqrt(input_tensor)

print(result_tensor)