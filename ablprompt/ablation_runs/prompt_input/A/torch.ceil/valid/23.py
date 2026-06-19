import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.2, 2.5, 3.7])

# Call torch.ceil to round up each element in the tensor
result = torch.ceil(tensor)

print(result)