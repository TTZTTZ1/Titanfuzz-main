import torch

# Create a tensor with some values
tensor = torch.tensor([-1.5, 0.2, 3.7])

# Clamp the tensor values between -1 and 2
clamped_tensor = torch.clamp(tensor, min=-1, max=2)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)