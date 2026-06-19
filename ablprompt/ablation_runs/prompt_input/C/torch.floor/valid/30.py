import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.5, -1.3, 0.7, -0.9], dtype=torch.float32)

# Apply torch.floor to the tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after floor:", output_tensor)