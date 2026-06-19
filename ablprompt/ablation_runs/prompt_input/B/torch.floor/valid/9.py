import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.3, -1.7, 0.5, -0.2])

# Apply torch.floor to the tensor
result_tensor = torch.floor(input_tensor)

print(result_tensor)