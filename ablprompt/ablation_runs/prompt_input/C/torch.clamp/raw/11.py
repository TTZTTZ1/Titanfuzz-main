import torch

# Create a tensor with values both below and above the clamp limits
input_tensor = torch.tensor([-10, 0, 5, 10, 15], dtype=torch.float32)

# Clamp the tensor values between -5 and 10
clamped_tensor = torch.clamp(input_tensor, min=-5, max=10)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)