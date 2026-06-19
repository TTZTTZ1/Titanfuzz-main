import torch

# Create a random tensor with floating-point values
input_tensor = torch.tensor([1.5, -2.3, 4.7, -0.8], dtype=torch.float32)

# Apply torch.floor to the input tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)