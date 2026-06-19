import torch

# Create a random tensor
input_tensor = torch.randn(4, 5)

# Define the new shape
new_shape = (2, 10)

# Reshape the tensor
reshaped_tensor = torch.reshape(input_tensor, new_shape)

print("Original Tensor Shape:", input_tensor.shape)
print("Reshaped Tensor Shape:", reshaped_tensor.shape)