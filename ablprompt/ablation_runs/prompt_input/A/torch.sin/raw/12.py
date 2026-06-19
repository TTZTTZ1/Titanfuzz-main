import torch

# Create a tensor of values
x = torch.tensor([0.0, 1.0, 2.0, 3.0])

# Compute the sine of each element in the tensor
result = torch.sin(x)

print(result)