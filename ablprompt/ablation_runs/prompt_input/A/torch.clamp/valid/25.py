import torch

# Create a tensor
tensor = torch.tensor([-1.0, 2.5, -3.0, 4.5])

# Clamp the tensor values between -2 and 3
clamped_tensor = torch.clamp(tensor, min=-2, max=3)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)