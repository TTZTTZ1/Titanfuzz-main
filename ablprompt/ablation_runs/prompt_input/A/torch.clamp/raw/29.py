import torch

# Create a tensor with values outside the clamp range
tensor = torch.tensor([-1.0, 2.5, 3.0])

# Clamp the tensor values between -1 and 3
clamped_tensor = torch.clamp(tensor, min=-1, max=3)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)