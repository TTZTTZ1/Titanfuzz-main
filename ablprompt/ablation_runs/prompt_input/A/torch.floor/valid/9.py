import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([2.5, 3.7, -1.2, 0.8])

# Apply the floor function to the tensor
floored_tensor = torch.floor(tensor)

print(floored_tensor)