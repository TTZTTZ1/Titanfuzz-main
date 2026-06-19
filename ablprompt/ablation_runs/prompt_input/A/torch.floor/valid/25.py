import torch

# Create a tensor with floating-point numbers
x = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Apply the floor function to the tensor
y = torch.floor(x)

print(y)