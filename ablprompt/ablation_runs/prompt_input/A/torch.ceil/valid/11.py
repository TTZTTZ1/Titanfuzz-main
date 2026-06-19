import torch

# Create a tensor with floating-point numbers
x = torch.tensor([1.2, 3.5, -0.8, 4.0])

# Call the torch.ceil function to round up each element in the tensor
y = torch.ceil(x)

print(y)