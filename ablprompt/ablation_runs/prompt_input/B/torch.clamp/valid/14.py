import torch

# Create a random tensor with values between -10 and 10
input_tensor = torch.randn(3, 4) * 20

# Clamp the tensor values between -5 and 5
clamped_tensor = torch.clamp(input_tensor, min=-5, max=5)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)