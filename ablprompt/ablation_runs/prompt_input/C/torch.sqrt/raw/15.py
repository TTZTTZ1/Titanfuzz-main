import torch

# Create a sample tensor with negative values to demonstrate handling of nan
input_tensor = torch.tensor([-1.0, 4.0, 9.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
result_tensor = torch.sqrt(input_tensor)

print(result_tensor)