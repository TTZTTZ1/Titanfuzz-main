import torch

# Generate a tensor with floating-point values
input_tensor = torch.tensor([1.0, 2.0, float('inf'), -float('inf'), float('nan')])

# Check if all elements of the tensor are finite
result = torch.isfinite(input_tensor)
print(result)