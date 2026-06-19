import torch

# Create a tensor
tensor = torch.randn(4, 4)

# Reshape the tensor to have 2 rows and 8 columns
reshaped_tensor = torch.reshape(tensor, (2, 8))

print(reshaped_tensor)