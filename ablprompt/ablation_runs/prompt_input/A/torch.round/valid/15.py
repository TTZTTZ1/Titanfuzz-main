import torch

# Create a tensor with floating-point values
tensor = torch.tensor([1.2, 3.5, -4.7])

# Round the elements of the tensor to the nearest integer
rounded_tensor = torch.round(tensor)

print("Original Tensor:", tensor)
print("Rounded Tensor:", rounded_tensor)