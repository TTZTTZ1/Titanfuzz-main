import torch

# Create a tensor with values for which we want to compute the tangent
x = torch.tensor([-1.0, 0.0, 1.0])

# Compute the tangent of each element in the tensor
tan_x = torch.tan(x)

print("Input tensor:", x)
print("Tangent of input tensor:", tan_x)