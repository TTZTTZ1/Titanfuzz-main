import torch

# Create a random tensor with both positive, negative, and zero values
input_tensor = torch.randn(5) * 10  # Random numbers between -10 and 10
signed_tensor = torch.sign(input_tensor)

print("Input Tensor:", input_tensor)
print("Signed Tensor:", signed_tensor)