import torch

# Create a tensor with values outside the desired range
input_tensor = torch.tensor([-1.0, 0.5, 1.5, 2.0])

# Clamp the tensor values between -0.5 and 1.0
clamped_tensor = torch.clamp(input_tensor, min=-0.5, max=1.0)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)