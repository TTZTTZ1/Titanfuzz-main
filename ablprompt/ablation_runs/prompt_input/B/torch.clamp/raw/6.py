import torch

# Create a random tensor with values between -10 and 10
input_tensor = torch.randn(5, 5) * 20 - 10

# Clamp the tensor to the range [-5, 5]
clamped_tensor = torch.clamp(input_tensor, min=-5, max=5)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)