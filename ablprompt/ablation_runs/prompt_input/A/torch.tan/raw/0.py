import torch

# Create a tensor
x = torch.tensor([0.0, 1.0, -1.0])

# Compute the tangent of each element in the tensor
tan_x = torch.tan(x)

print(tan_x)