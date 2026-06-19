import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.2, 2.5, 3.7, 4.1])

# Use torch.round to round the elements of the tensor
rounded_tensor = torch.round(tensor)

print(rounded_tensor)