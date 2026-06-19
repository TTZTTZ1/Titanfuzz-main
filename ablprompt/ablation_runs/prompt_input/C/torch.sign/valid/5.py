import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(5)

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(input_tensor)

print("Input Tensor:", input_tensor)
print("Signed Tensor:", signed_tensor)