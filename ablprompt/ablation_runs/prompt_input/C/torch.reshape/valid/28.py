import torch

# Create a random tensor
input_tensor = torch.randn(6)

# Reshape the tensor to a 3x2 matrix
reshaped_tensor = torch.reshape(input_tensor, (3, 2))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)