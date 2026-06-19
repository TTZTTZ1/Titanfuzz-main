import torch

# Create a tensor
tensor = torch.randn(4, 4)

# Reshape the tensor
reshaped_tensor = torch.reshape(tensor, (2, 8))

print(reshaped_tensor)