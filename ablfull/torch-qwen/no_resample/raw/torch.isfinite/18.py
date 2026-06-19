import torch

# Generate a tensor with finite values to satisfy the isfinite check
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the torch.isfinite API
result = torch.isfinite(input_tensor)
print(result)