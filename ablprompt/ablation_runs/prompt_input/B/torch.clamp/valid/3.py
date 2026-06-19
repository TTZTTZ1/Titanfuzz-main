import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Define min and max values for clamping
min_value = -0.5
max_value = 0.5

# Clamp the tensor values between -0.5 and 0.5
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)