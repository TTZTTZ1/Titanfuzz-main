import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Call torch.argmax to find the indices of the maximum values along the specified dimension
result = torch.argmax(tensor, dim=1)

print(result)