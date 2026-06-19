import torch

# Create a random tensor with positive values
input_tensor = torch.tensor([4.0, 9.0, 16.0], dtype=torch.float32)

# Compute the square root of the input tensor
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)