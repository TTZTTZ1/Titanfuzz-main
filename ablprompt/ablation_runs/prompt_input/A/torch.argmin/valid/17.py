import torch

# Create a tensor
tensor = torch.tensor([[10, 20], [30, 40]])

# Use torch.argmin to find the index of the minimum value in the tensor
result = torch.argmin(tensor)

print(result)