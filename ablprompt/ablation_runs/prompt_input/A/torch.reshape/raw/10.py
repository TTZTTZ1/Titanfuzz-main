import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Reshape the tensor
reshaped_tensor = torch.reshape(tensor, (4,))

print(reshaped_tensor)