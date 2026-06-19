import torch

# Create a random tensor with shape (4, 5)
input_tensor = torch.randn(4, 5)

# Reshape the tensor to (2, 10)
reshaped_tensor = torch.reshape(input_tensor, (2, 10))

print("Original Tensor:", input_tensor)
print("Reshaped Tensor:", reshaped_tensor)