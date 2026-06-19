import torch

# Generate a tensor with float32 type containing both finite and non-finite values
input_tensor = torch.tensor([1.0, -float('inf'), 2.0, float('nan')], dtype=torch.float32)

# Check if all elements in the tensor are finite
result = torch.isfinite(input_tensor)
print(result)