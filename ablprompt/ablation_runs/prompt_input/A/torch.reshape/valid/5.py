import torch

# Create a tensor
tensor = torch.randn(4, 4)

# Reshape the tensor to (2, 8)
reshaped_tensor = torch.reshape(tensor, (2, 8))

print(reshaped_tensor)