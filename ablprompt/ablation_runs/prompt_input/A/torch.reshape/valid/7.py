import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Reshape the tensor to have 4 elements in a single row
reshaped_tensor = torch.reshape(tensor, (1, 4))

print(reshaped_tensor)