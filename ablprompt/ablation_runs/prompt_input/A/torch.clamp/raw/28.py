import torch

# Create a tensor with some values
tensor = torch.tensor([-1.5, 0.2, 3.7])

# Use torch.clamp to clamp the values between -1 and 1
clamped_tensor = torch.clamp(tensor, min=-1, max=1)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)