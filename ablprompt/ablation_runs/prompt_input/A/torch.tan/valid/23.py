import torch

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0])

# Compute tangent of each element in the tensor
result = torch.tan(x)

print(result)