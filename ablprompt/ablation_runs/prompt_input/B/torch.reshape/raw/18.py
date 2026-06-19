import torch

# Create a random tensor
input_tensor = torch.randn(4, 3)

# Reshape the tensor to a different shape
reshaped_tensor = torch.reshape(input_tensor, (-1, 6))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)