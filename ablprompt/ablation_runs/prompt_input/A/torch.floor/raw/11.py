import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([2.5, 3.14, -1.7, 0.0])

# Apply the floor function to the tensor
floored_tensor = torch.floor(tensor)

print("Original Tensor:", tensor)
print("Floored Tensor:", floored_tensor)