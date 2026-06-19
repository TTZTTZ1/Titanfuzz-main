import torch

# Create a random tensor with 12 elements
input_tensor = torch.randn(3, 4)

# Reshape the tensor to 6x2
reshaped_tensor = torch.reshape(input_tensor, (6, 2))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)