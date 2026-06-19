import torch

# Create a random tensor
input_tensor = torch.randn(4, 5)

# Reshape the tensor to a new shape
reshaped_tensor = torch.reshape(input_tensor, (-1,))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)