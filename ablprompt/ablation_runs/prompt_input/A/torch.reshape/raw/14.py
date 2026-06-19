import torch

# Create a tensor
tensor = torch.arange(12)

# Reshape the tensor to 3x4
reshaped_tensor = torch.reshape(tensor, (3, 4))

print(reshaped_tensor)