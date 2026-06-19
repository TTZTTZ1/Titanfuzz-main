import torch

# Create a tensor with mixed data types
mixed_tensor = torch.tensor([-2, 0, 3, -4], dtype=torch.float)

# Apply torch.sign to get the sign of each element
signed_tensor = torch.sign(mixed_tensor)

print(signed_tensor)