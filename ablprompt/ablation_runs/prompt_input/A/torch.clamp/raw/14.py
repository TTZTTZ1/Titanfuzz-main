import torch

# Create a tensor with values outside the desired range
tensor = torch.tensor([-1.0, 2.5, 3.0, -0.5])

# Clamp the tensor to be within the range [0, 2]
clamped_tensor = torch.clamp(tensor, min=0, max=2)

print("Original Tensor:", tensor)
print("Clamped Tensor:", clamped_tensor)