import torch

# Create a tensor with positive values
x = torch.tensor([4.0, 9.0, 16.0])

# Compute the square root of each element in the tensor
result = torch.sqrt(x)

print(result)