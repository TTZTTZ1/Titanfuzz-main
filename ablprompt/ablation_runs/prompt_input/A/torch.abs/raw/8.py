import torch

# Create a tensor with negative and positive values
tensor = torch.tensor([-1.0, 2.0, -3.0, 4.0])

# Apply the torch.abs function to get the absolute values of the tensor elements
abs_tensor = torch.abs(tensor)

print("Original Tensor:", tensor)
print("Absolute Values Tensor:", abs_tensor)