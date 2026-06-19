import torch

# Create a random tensor with floating-point values
input_tensor = torch.tensor([1.5, -2.3, 4.7, -0.8])

# Apply torch.floor to get the largest integers less than or equal to each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)