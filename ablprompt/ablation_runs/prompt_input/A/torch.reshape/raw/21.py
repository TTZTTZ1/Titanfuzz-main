import torch

# Create a tensor
tensor = torch.arange(8)

# Reshape the tensor to 2x4
reshaped_tensor = torch.reshape(tensor, (2, 4))

print(reshaped_tensor)