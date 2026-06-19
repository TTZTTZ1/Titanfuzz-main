import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 3)

# Clamp the tensor values between -1 and 1
clamped_tensor = torch.clamp(input_tensor, min=-1, max=1)

print("Original Tensor:")
print(input_tensor)
print("Clamped Tensor:")
print(clamped_tensor)