import torch

# Generate a tensor of random values to ensure it's finite
input_tensor = torch.rand(5, 5)

# Check if all elements in the tensor are finite
result = torch.isfinite(input_tensor)
print(result)