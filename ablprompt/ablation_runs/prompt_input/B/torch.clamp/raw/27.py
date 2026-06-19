import torch

# Create a random tensor with values between -5 and 5
input_tensor = torch.randn(3, 4) * 10

# Clamp the tensor values between -2 and 2
clamped_tensor = torch.clamp(input_tensor, min=-2, max=2)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)