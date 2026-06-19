import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Define the new shape
new_shape = (6, 2)

# Reshape the tensor
reshaped_tensor = torch.reshape(input_tensor, new_shape)

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)