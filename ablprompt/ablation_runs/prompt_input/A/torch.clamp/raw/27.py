import torch

# Create a tensor with some values
tensor = torch.tensor([-1.5, 0.3, 2.7])

# Clamp the tensor between -1 and 1
clamped_tensor = torch.clamp(tensor, min=-1, max=1)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)