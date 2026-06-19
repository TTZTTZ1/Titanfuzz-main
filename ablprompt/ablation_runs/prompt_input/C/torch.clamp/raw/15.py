import torch

# Create a sample tensor
input_tensor = torch.tensor([-1.0, 0.5, 2.0, 3.5], dtype=torch.float)

# Clamp the tensor values between -0.5 and 2.5
clamped_tensor = torch.clamp(input_tensor, min=-0.5, max=2.5)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)