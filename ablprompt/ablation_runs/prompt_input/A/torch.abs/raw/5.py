import torch

# Create a tensor with both positive and negative values
tensor = torch.tensor([-1.0, 2.0, -3.0, 4.0])

# Apply the torch.abs function to compute the absolute values of the tensor elements
absolute_tensor = torch.abs(tensor)

print("Original Tensor:", tensor)
print("Absolute Tensor:", absolute_tensor)