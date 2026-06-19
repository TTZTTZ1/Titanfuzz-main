import torch

# Generate a tensor with finite values
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Check if all elements in the tensor are finite
result = torch.isfinite(input_tensor)
print(result)