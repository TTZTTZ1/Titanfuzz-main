import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.7, -2.5, 0.9])

# Apply torch.floor to the tensor
output_tensor = torch.floor(input_tensor)

print(output_tensor)