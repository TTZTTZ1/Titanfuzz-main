import torch

# Create a tensor with mixed values
mixed_tensor = torch.tensor([-3.5, 0.0, 4.2, -6])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(mixed_tensor)

print("Original Tensor:", mixed_tensor)
print("Signed Tensor:", signed_tensor)