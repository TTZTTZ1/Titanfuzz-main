import torch

# Create a tensor with both positive, negative, and zero values
input_tensor = torch.tensor([-5, 0, 5], dtype=torch.float)

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(input_tensor)

print("Input Tensor:", input_tensor)
print("Signed Tensor:", signed_tensor)