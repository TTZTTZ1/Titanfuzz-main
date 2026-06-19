import torch

# Create a tensor with some values
tensor = torch.tensor([-1.0, 2.0, 3.0, -4.0])

# Use torch.clamp to clamp the tensor values between -2 and 2
clamped_tensor = torch.clamp(tensor, min=-2, max=2)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)