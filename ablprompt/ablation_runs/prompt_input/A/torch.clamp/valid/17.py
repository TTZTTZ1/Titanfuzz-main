import torch

# Create a tensor with some values
tensor = torch.tensor([-1.0, 2.0, 3.0, -4.0])

# Clamp the tensor between 0 and 2
clamped_tensor = torch.clamp(tensor, min=0, max=2)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)