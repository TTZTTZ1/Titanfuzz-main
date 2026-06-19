import torch

# Create a random tensor of floats between 0 and 2*pi
input_tensor = torch.rand(5) * 2 * torch.pi

# Compute the cosine of each element in the tensor
output_tensor = torch.cos(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)