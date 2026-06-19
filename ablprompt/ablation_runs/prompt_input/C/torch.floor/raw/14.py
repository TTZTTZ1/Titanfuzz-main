import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Apply torch.floor to get the floor values
result_tensor = torch.floor(input_tensor)

print(result_tensor)