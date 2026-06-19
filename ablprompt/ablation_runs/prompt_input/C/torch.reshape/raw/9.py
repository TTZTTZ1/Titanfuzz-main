import torch

# Create a random tensor
input_tensor = torch.randn(4, 3)

# Reshape the tensor to (6, 2)
reshaped_tensor = torch.reshape(input_tensor, (6, 2))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)