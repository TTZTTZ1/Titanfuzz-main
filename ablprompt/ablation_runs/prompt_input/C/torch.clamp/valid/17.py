import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 3)

# Clamp the tensor values between -0.5 and 0.5
clamped_tensor = torch.clamp(input_tensor, min=-0.5, max=0.5)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)