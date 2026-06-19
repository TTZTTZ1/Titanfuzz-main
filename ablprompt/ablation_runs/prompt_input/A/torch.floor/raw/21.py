import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.5, 2.3, 4.7, -1.2])

# Apply the floor function to the tensor
floored_tensor = torch.floor(tensor)

print(floored_tensor)