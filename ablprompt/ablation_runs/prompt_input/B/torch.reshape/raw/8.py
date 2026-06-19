import torch

# Create a random tensor
input_tensor = torch.randn(4, 5)

# Define the desired shape
desired_shape = (-1, 10)

# Reshape the tensor
reshaped_tensor = torch.reshape(input_tensor, desired_shape)

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)