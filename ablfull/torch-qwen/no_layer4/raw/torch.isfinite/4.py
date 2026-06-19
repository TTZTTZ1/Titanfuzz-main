import torch

# Create a tensor with finite values of various dtypes
input_tensor = torch.tensor([1.0, 2.0, float('inf'), -float('inf')], dtype=torch.float32)

# Check if all elements in the tensor are finite
result = torch.isfinite(input_tensor)
print(result)