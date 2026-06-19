import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.5, -2.3, 4.7, -6.8])

# Apply torch.floor to get the largest integer less than or equal to each element
result_tensor = torch.floor(input_tensor)

print(result_tensor)