import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.5, -1.3, 4.8, -0.7])

# Apply torch.floor to get the largest integers less than or equal to each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)