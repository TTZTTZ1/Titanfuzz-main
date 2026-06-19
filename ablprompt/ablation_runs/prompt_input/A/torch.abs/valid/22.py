import torch

# Create a tensor with negative and positive values
tensor = torch.tensor([-1.0, 2.0, -3.0, 4.0])

# Use torch.abs to compute the absolute values of the tensor elements
abs_tensor = torch.abs(tensor)

print(abs_tensor)