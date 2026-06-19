import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.2, 2.5, 3.7])

# Apply the ceil function to round up each element
ceiled_tensor = torch.ceil(tensor)

print("Original Tensor:", tensor)
print("Ceiled Tensor:", ceiled_tensor)