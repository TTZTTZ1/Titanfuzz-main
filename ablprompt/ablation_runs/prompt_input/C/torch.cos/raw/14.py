import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(5, 5, dtype=torch.float32)

# Compute the cosine of each element in the input tensor
output_tensor = torch.cos(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Cosine Output Tensor:")
print(output_tensor)