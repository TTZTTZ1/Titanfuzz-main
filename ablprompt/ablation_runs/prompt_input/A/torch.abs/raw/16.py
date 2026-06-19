import torch

# Create a tensor with both positive and negative values
tensor = torch.tensor([-1.0, 2.0, -3.0, 4.0])

# Call the torch.abs function to get the absolute values of the tensor elements
abs_tensor = torch.abs(tensor)

print(abs_tensor)