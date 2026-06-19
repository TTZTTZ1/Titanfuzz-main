import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, -3.7, 4.5, -6.8])

# Apply torch.floor to get the largest integer less than or equal to each element
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying torch.floor:", output_tensor)