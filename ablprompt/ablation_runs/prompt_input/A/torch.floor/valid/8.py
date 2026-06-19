import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Apply the floor function to the tensor
result = torch.floor(tensor)

print(result)