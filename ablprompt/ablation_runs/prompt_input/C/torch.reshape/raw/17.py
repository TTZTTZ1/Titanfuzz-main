import torch

# Create a random tensor
input_tensor = torch.randn(4, 3)

# Reshape the tensor to a new shape
reshaped_tensor = torch.reshape(input_tensor, (-1,))

print("Original Tensor Shape:", input_tensor.shape)
print("Reshaped Tensor Shape:", reshaped_tensor.shape)