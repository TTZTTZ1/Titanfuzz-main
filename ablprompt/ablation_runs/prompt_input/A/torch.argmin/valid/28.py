import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 0]])

# Use torch.argmin to find the index of the minimum value in the tensor
result = torch.argmin(tensor)

print(result)