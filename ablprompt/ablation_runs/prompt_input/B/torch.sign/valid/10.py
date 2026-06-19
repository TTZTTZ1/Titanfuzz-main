import torch

# Create a tensor with mixed data types
mixed_tensor = torch.tensor([-2, 0, 3], dtype=torch.float)

# Apply torch.sign to the tensor
signed_tensor = torch.sign(mixed_tensor)

print(signed_tensor)