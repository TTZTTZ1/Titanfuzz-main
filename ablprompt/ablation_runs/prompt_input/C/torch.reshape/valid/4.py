import torch

# Create a random tensor with 24 elements
input_tensor = torch.randn(6, 4)

# Reshape the tensor to 3x8
reshaped_tensor = torch.reshape(input_tensor, (3, 8))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)