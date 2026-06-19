import torch

# Create a tensor with values outside the range [0, 1]
tensor = torch.tensor([-0.5, 2.0, 0.3])

# Clamp the tensor to be within the range [0, 1]
clamped_tensor = torch.clamp(tensor, min=0, max=1)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)