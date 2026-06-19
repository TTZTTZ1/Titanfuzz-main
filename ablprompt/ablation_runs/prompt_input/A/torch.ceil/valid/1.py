import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([-1.2, 3.5, -4.8, 5.0])

# Apply the torch.ceil function to the tensor
ceiled_tensor = torch.ceil(tensor)

print("Original Tensor:", tensor)
print("Ceiled Tensor:", ceiled_tensor)