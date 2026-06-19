import torch

# Create a tensor with values outside the clamp range
tensor = torch.tensor([-1.0, 2.0, 3.5])

# Clamp the tensor to be within the range [0, 3]
clamped_tensor = torch.clamp(tensor, min=0, max=3)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)