import torch

# Create a tensor with floating-point values
tensor = torch.tensor([2.5, 3.14, -1.7])

# Apply the floor function to each element in the tensor
floored_tensor = torch.floor(tensor)

print(floored_tensor)