import torch

# Create a tensor with some finite values
input_tensor = torch.tensor([1.0, 2.0, float('inf'), -float('inf')], dtype=torch.float32)

# Check if all elements are finite
result = torch.isfinite(input_tensor)
print(result)