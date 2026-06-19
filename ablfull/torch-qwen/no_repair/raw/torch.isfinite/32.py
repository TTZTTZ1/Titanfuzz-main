import torch

# Generate a tensor of random values
input_tensor = torch.randn(3, 3)

# Check if all elements in the tensor are finite
result = torch.isfinite(input_tensor)
print(result)