import torch

# Create a tensor with floating-point values
tensor = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Apply the floor function to round down each element to the nearest integer
floored_tensor = torch.floor(tensor)

print("Original Tensor:", tensor)
print("Floored Tensor:", floored_tensor)