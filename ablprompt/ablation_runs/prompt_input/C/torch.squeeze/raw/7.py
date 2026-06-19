import torch

# Create a tensor with an extra singleton dimension
input_tensor = torch.randn(3, 1, 4, 1)

# Squeeze out the singleton dimensions
squeezed_tensor = torch.squeeze(input_tensor)

print("Original Tensor Shape:", input_tensor.shape)
print("Squeezed Tensor Shape:", squeezed_tensor.shape)