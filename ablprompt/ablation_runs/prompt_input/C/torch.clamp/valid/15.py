import torch

# Create a sample tensor
input_tensor = torch.tensor([-1.5, 0.0, 2.5, 4.0])

# Clamp the tensor values between -1 and 3
clamped_tensor = torch.clamp(input_tensor, min=-1, max=3)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)