import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply torch.floor to the tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)